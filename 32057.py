
import sys
input = sys.stdin.readline

def check(s):
    S = [None] * M 
    for (X, T) in s:
        pos = X - 1
        for ch in T:
            if S[pos] is None:
                S[pos] = ch
            else:
                if S[pos] != ch:
                    return None
            pos += 1
    if any(ch is None for ch in S):
        return None
    return "".join(S)

n, M = map(int, input().split())
hints = []
for _ in range(n):
    li = input().split()
    X = int(li[0])
    T = li[1].strip()
    hints.append((X, T))


set = set()

sol = check(hints)
if sol is not None:
    set.add(sol)

for i in range(n):
    selected = hints[:i] + hints[i+1:]
    sol = check(selected)
    if sol is not None:
        set.add(sol)

if len(set) == 0:
    print(-1)
elif len(set) == 1:
    print(set.pop())
else:
    print(-2)
