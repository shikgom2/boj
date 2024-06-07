import re
import sys
from math import gcd

e = [10**i for i in range(10)]
pattern = re.compile(r"([0-9]+)\.([0-9]*)\(([0-9]+)\)")

for line in sys.stdin:
    s = line.strip()
    match = pattern.match(s)
    if match:
        n1 = int(match.group(1) + match.group(2))
        n2 = int(match.group(3))
        p1 = e[len(match.group(2))]
        p2 = e[len(match.group(3))]
        num = n1 * (p2 - 1) + n2
        denom = p1 * (p2 - 1)
        div = gcd(num, denom)
        print(f"{s} = {num // div} / {denom // div}")
