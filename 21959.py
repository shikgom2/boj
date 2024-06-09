import sys
input = sys.stdin.readline

k = int(input())
vp = [(0, -1)]
ans = 0

while ans + len(vp) <= k:
    ans += len(vp)
    vp.append((len(vp), len(vp) - 1))

if ans != k:
    vp.append((len(vp), k - ans - 1))

print(len(vp))
for i in vp:
    print(i[0], i[1])