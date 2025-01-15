import sys
input = sys.stdin.readline 
A,B,C = map(int, input().split())


if A + B == C:
    print(f"{A}+{B}={C}")
    exit()
if A - B == C:
    print(f"{A}-{B}={C}")
    exit()
if A * B == C:
    print(f"{A}*{B}={C}")
    exit()
if B != 0 and A % B == 0 and A // B == C:
    print(f"{A}/{B}={C}")
    exit()

if A == B + C:
    print(f"{A}={B}+{C}")
    exit()
if A == B - C:
    print(f"{A}={B}-{C}")
    exit()
if A == B * C:
    print(f"{A}={B}*{C}")
    exit()
if C != 0 and B % C == 0 and B // C == A:
    print(f"{A}={B}/{C}")
    exit()
