import sys
input = sys.stdin.readline

n = int(input())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

u = sum(li1)
d = sum(li2)

pre = -10**18
pu, pd = 0, 0
for i in range(n):
    pu += li1[i]
    pd += li2[i]
    pre = max(pre, pd - pu)

cand1 = u + pre

suf = -10**18
su, sd = 0, 0
for i in range(n-1, -1, -1):
    su += li1[i]
    sd += li2[i]
    suf = max(suf, su - sd)

cand2 = d + suf

ans = min(cand1, cand2) - (u + d)
print(ans)
