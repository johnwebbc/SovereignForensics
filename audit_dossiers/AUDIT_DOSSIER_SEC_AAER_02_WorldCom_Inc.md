I'll verify the arithmetic and hash with real tool runs first, then write the dossier.




Bash
{
  "command": "python -c \"import z3, sys; print('z3', z3.get_version_string(), sys.version.split()[0])\" 2>&1; python - <<'EOF'\nimport hashlib, json\nfin = {\"assets\": 103914000000.0, \"liabilities\": 51648000000.0, \"equity\": 52266000000.0, \"net_income\": 4013000000.0, \"cfo\": 7674000000.0, \"accruals\": -3661000000.0}\ncanon = json.dumps(fin, sort_keys=True, separators=(',',':'))\nprint(canon)\nprint('sha256', hashlib.sha256(canon.encode()).hexdigest())\nprint('bs', fin['liabilities']+fin['equity']==fin['assets'])\nprint('accr', fin['net_income']-fin['cfo'])\nprint('sloan', fin['accruals']/fin['assets'])\nprint('split', 3055e6+797e6)\nEOF"
}


Bash
{
  "command": "mkdir -p /tmp/wcom && cat > /tmp/wcom/z3_proof.py <<'EOF'\nfrom z3 import *\n\n# --- Dataset constants (USD, exact rationals) ---\nASSETS      = RealVal(103_914_000_000)\nLIABILITIES = RealVal( 51_648_000_000)\nEQUITY      = RealVal( 52_266_000_000)\nNET_INCOME  = RealVal(  4_013_000_000)\nCFO         = RealVal(  7_674_000_000)\nACCRUALS    = RealVal( -3_661_000_000)\nCAP_FY2001  = RealVal(  3_055_000_000)   # line costs capitalized FY2001 (AAER)\nCAP_Q12002  = RealVal(    797_000_000)   # line costs capitalized Q1 2002 (AAER)\nMISSTATE    = RealVal(  3_852_000_000)   # asserted aggregate\n\ndef prove(name, claim):\n    s = Solver(); s.add(Not(claim)); r = s.check()\n    print(f\"[{'PROVED' if r == unsat else 'FAILED'}] {name}\")\n    if r != unsat: print(\"   counterexample:\", s.model())\n    return r == unsat\n\nresults = []\n# Invariant 1: balance-sheet identity A = L + E\nresults.append(prove(\"I1 A == L + E\", ASSETS == LIABILITIES + EQUITY))\n# Invariant 2: accrual identity NI - CFO = ACCRUALS\nresults.append(prove(\"I2 NI - CFO == ACCRUALS\", NET_INCOME - CFO == ACCRUALS))\n# Invariant 3: AAER components sum to asserted misstatement\nresults.append(prove(\"I3 3,055M + 797M == 3,852M\", CAP_FY2001 + CAP_Q12002 == MISSTATE))\n\n# Invariant 4 (recovery/restatement bound): for ANY effective tax rate t in [0, 0.40],\n# reversing capitalized line costs reduces pre-tax income by exactly MISSTATE and\n# after-tax income by at least 0.60 * MISSTATE; PP&E falls by MISSTATE.\nt = Real('t'); restated_ni = Real('restated_ni'); ppe_delta = Real('ppe_delta')\nmodel = And(t >= 0, t <= RealVal(\"0.40\"),\n            restated_ni == NET_INCOME - MISSTATE * (1 - t),\n            ppe_delta == -MISSTATE)\nbound = And(restated_ni <= NET_INCOME - RealVal(\"0.60\") * MISSTATE,\n            ppe_delta == RealVal(-3_852_000_000))\nresults.append(prove(\"I4 restated NI <= NI - 0.60*3,852M for all t in [0,0.40]\", Implies(model, bound)))\n\n# Counterexample C1: metadata Sloan ratio 0.342 is NOT consistent with dataset\n# (ACCRUALS / ASSETS). Expect SAT = inconsistency exposed.\nsloan = Real('sloan'); s = Solver()\ns.add(sloan == ACCRUALS / ASSETS, Or(sloan - RealVal(\"0.342\") > RealVal(\"0.001\"), RealVal(\"0.342\") - sloan > RealVal(\"0.001\")))\nr = s.check()\nprint(f\"[{'SAT' if r == sat else r}] C1 dataset Sloan ratio != 0.342 (metadata figure inconsistent)\")\nif r == sat: print(\"   dataset Sloan =\", s.model()[sloan].as_decimal(6))\n\n# Counterexample C2: an honest model (capitalized line cost == 0) cannot reproduce\n# a PP&E carrying value that includes the 3,852M. SAT => the only consistent world\n# is the one with the capitalization.\cap = Real('cap'); ppe_rep = Real('ppe_rep'); ppe_true = Real('ppe_true'); s2 = Solver()\ns2.add(ppe_rep == ppe_true + cap, ppe_rep - ppe_true == MISSTATE, cap == 0)\nprint(f\"[{s2.check()}] C2 honest model (cap==0) with observed PP&E overstatement -> expect unsat\")\ns3 = Solver(); s3.add(ppe_rep == ppe_true + cap, ppe_rep - ppe_true == MISSTATE)\nprint(f\"[{s3.check()}] C2' fraud model (cap free) -> expect sat; cap =\", end=\" \")\nprint(s3.model()[cap] if s3.check() == sat else None)\n\nprint(\"ALL INVARIANTS PROVED:\", all(results))\nEOF\nsed -i 's/\\\\cap = Real/cap = Real/' /tmp/wcom/z3_proof.py\npython /tmp/wcom/z3_proof.py 2>&1"
}


Bash
{
  "command": "cat > /tmp/wcom/z3_proof.py <<'EOF'\nfrom z3 import *

# --- Dataset constants (USD, exact rationals) ---
ASSETS      = RealVal(103_914_000_000)
LIABILITIES = RealVal( 51_648_000_000)
EQUITY      = RealVal( 52_266_000_000)
NET_INCOME  = RealVal(  4_013_000_000)
CFO         = RealVal(  7_674_000_000)
ACCRUALS    = RealVal( -3_661_000_000)
CAP_FY2001  = RealVal(  3_055_000_000)   # line costs capitalized FY2001 (AAER)
CAP_Q12002  = RealVal(    797_000_000)   # line costs capitalized Q1 2002 (AAER)
MISSTATE    = RealVal(  3_852_000_000)   # asserted aggregate

def prove(name, claim):
    s = Solver(); s.add(Not(claim)); r = s.check()
    print(f"[{'PROVED' if r == unsat else 'FAILED'}] {name}")
    if r != unsat: print("   counterexample:", s.model())
    return r == unsat

results = []
results.append(prove("I1 A == L + E", ASSETS == LIABILITIES + EQUITY))
results.append(prove("I2 NI - CFO == ACCRUALS", NET_INCOME - CFO == ACCRUALS))
results.append(prove("I3 3,055M + 797M == 3,852M", CAP_FY2001 + CAP_Q12002 == MISSTATE))

t = Real('t'); restated_ni = Real('restated_ni'); ppe_delta = Real('ppe_delta')
model = And(t >= 0, t <= RealVal("0.40"),
            restated_ni == NET_INCOME - MISSTATE * (1 - t),
            ppe_delta == -MISSTATE)
bound = And(restated_ni <= NET_INCOME - RealVal("0.60") * MISSTATE,
            ppe_delta == RealVal(-3_852_000_000))
results.append(prove("I4 restated NI <= NI - 0.60*3,852M for all t in [0,0.40]", Implies(model, bound)))

sloan = Real('sloan'); s = Solver()
s.add(sloan == ACCRUALS / ASSETS,
      Or(sloan - RealVal("0.342") > RealVal("0.001"), RealVal("0.342") - sloan > RealVal("0.001")))
r = s.check()
print(f"[{'SAT' if r == sat else r}] C1 dataset Sloan ratio != 0.342 (metadata figure inconsistent)")
if r == sat: print("   dataset Sloan =", s.model()[sloan].as_decimal(6))

cap = Real('cap'); ppe_rep = Real('ppe_rep'); ppe_true = Real('ppe_true')
s2 = Solver(); s2.add(ppe_rep == ppe_true + cap, ppe_rep - ppe_true == MISSTATE, cap == 0)
print(f"[{s2.check()}] C2 honest model (cap==0) with observed PP&E overstatement -> expect unsat")
s3 = Solver(); s3.add(ppe_rep == ppe_true + cap, ppe_rep - ppe_true == MISSTATE)
r3 = s3.check()
print(f"[{r3}] C2' fraud model (cap free) -> expect sat; cap =", s3.model()[cap] if r3 == sat else None)

print("ALL INVARIANTS PROVED:", all(results))
EOF
python /tmp/wcom/z3_proof.py 2>&1; sha256sum /tmp/wcom/z3_proof.py"
}




Bash
{
  "command": "python -c \"import z3; print(z3.get_version_string())\"; python /tmp/wcom/z3_proof.py; sha256sum /tmp/wcom/z3_proof.py"
}




Bash
{
  "command": "cd /tmp/wcom && python z3_proof.py; echo \"exit=$?\"; sha256sum z3_proof.py; python -c \"import hashlib,json; fin={'assets':103914000000.0,'liabilities':51648000000.0,'equity':52266000000.0,'net_income':4013000000.0,'cfo':7674000000.0,'accruals':-3661000000.0}; c=json.dumps(fin,sort_keys=True,separators=(',',':')); print(c); print(hashlib.sha256(c.encode()).hexdigest()); print(fin['accruals']/fin['assets'])\""
}




Bash
{
  "command": "ls -la /tmp/wcom/ ; which python python3; python3 --version"
}




Bash
{
  "command": "cd /tmp/wcom && python3 z3_proof.py 2>&1 | head -30; echo \"exit=${PIPESTATUS[0]}\""
}




Bash
{
  "command": "cd /tmp/wcom && python3 -c \"print('hi')\"; python3 -c \"import z3; print(z3.get_version_string())\" 2>&1 | tail -2"
}




Bash
{
  "command": "cd /tmp/wcom && python3 z3_proof.py 2>&1; echo \"exit=$?\"; sha256sum z3_proof.py; python3 -c \"import hashlib,json; fin={'assets':103914000000.0,'liabilities':51648000000.0,'equity':52266000000.0,'net_income':4013000000.0,'cfo':7674000000.0,'accruals':-3661000000.0}; c=json.dumps(fin,sort_keys=True,separators=(',',':')); print(c); print(hashlib.sha256(c.encode()).hexdigest()); print(fin['accruals']/fin['assets'])\""
}




Bash
{
  "command": "cd /tmp/wcom && python3 z3_proof.py > out.txt 2>&1; echo \"exit=$?\"; cat out.txt"
}




Bash
{
  "command": "cat /tmp/wcom/out.txt; echo ---; sha256sum /tmp/wcom/z3_proof.py; echo ---; python3 -c \"import hashlib,json; fin={'assets':103914000000.0,'liabilities':51648000000.0,'equity':52266000000.0,'net_income':4013000000.0,'cfo':7674000000.0,'accruals':-3661000000.0}; c=json.dumps(fin,sort_keys=True,separators=(',',':')); print(c); print(hashlib.sha256(c.encode()).hexdigest()); print(fin['accruals']/fin['assets'])\" > /tmp/wcom/hash.txt 2>&1; cat /tmp/wcom/hash.txt"
}