import sys
input = sys.stdin.readline

N,P,Q,R = map(int, input().split())
v = list(map(str, input().rstrip()))

ans = 0
skh, sk, kh, sh = 0, 0, 0, 0
s, k, h = 0, 0, 0

pos = 0
while pos < N:
    if pos <= N - 3 and v[pos] == 'S' and v[pos + 1] == 'K' and v[pos + 2] == 'H':
        skh += 1
        pos += 3
    elif pos <= N - 2 and v[pos] == 'S' and v[pos + 1] == 'K':
        sk += 1
        pos += 2
    elif pos <= N - 2 and v[pos] == 'K' and v[pos + 1] == 'H':
        kh += 1
        pos += 2
    elif pos <= N - 2 and v[pos] == 'S' and v[pos + 1] == 'H':
        sh += 1
        pos += 2
    elif v[pos] == 'S':
        s += 1
        pos += 1
    elif v[pos] == 'K':
        k += 1
        pos += 1
    elif v[pos] == 'H':
        h += 1
        pos += 1

ans += skh
ans += min(sk, R) + min(kh, P) + min(sh, Q)
P -= min(kh, P)
Q -= min(sh, Q)
R -= min(sk, R)

maxi = 0
mini = min(s, Q, R)
for i in range(mini + 1):
    t1 = min(k, P, R - i)
    t2 = min(h, P - t1, Q - i)
    t3 = min(P - t1 - t2, Q - i - t2, R - i - t1)
    maxi = max(maxi, i + t1 + t2 + t3)

mini = min(k, P, R)
for i in range(mini + 1):
    t1 = min(s, Q, R - i)
    t2 = min(h, P - i, Q - t1)
    t3 = min(P - i - t2, Q - t1 - t2, R - i - t1)
    maxi = max(maxi, i + t1 + t2 + t3)

mini = min(h, P, Q)
for i in range(mini + 1):
    t1 = min(s, Q - i, R)
    t2 = min(k, P - i, R - t1)
    t3 = min(P - i - t2, Q - i - t1, R - t1 - t2)
    maxi = max(maxi, i + t1 + t2 + t3)

ans += maxi
print(ans)