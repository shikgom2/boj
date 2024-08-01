t = int(input())
li = list(map(int, input().split())) + [0 for _ in range(5)]
ans = 0
K = li[0]
E = li[2]
M = li[1]
S = li[3]
F = li[4]
if K > E:
    ans += (K - E) * 508
else:
    ans += (E - K) * 108

if M > S:
    ans += (M - S) * 212
else:
    ans += (S - M) * 305
ans += F * 707
print(ans * 4763)