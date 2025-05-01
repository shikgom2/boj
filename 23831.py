import sys
input = sys.stdin.readline

n = int(input())
INF = 10**9

li = []
k = 1
while True:
    v = (10**k - 1) // 9
    if v > n:
        break
    li.append((v, k))
    k += 1

dp_len = [INF] * (n + 1)
dp = ['']  * (n + 1)
flag = [False] * (n + 1)
plus = [False] * (n + 1)
multi = [False] * (n + 1)


for v, k in li:
    dp_len[v] = k
    dp[v]     = '1' * k
    flag[v]   = True

if dp_len[1] == INF:
    dp_len[1] = 1
    dp[1]     = '1'
    flag[1]   = True

for m in range(2, n + 1):
    best_len = dp_len[m]
    best_op  = None
    best_a = best_b = 0

    # 덧셈
    for a in range(1, m // 2 + 1):
        b = m - a
        la = dp_len[a]
        lb = dp_len[b]
        if la < INF and lb < INF:
            tmp = la + 1 + lb
            if tmp < best_len:
                best_len = tmp
                best_op  = '+'
                best_a, best_b = a, b

    d = 2
    while d * d <= m:
        if m % d == 0:
            a = d
            b = m // d
            la = dp_len[a]
            lb = dp_len[b]
            if la < INF and lb < INF:
                od = (2 if plus[a] else 0) + (2 if (plus[b] or multi[b]) else 0)
                tmp = la + 1 + lb + od
                if tmp < best_len:
                    best_len = tmp
                    best_op  = '*'
                    best_a, best_b = a, b
        d += 1

    if best_len < dp_len[m]:
        dp_len[m] = best_len
        a, b = best_a, best_b
        if best_op == '+':
            dp[m]   = dp[a] + '+' + dp[b]
            flag[m] = False
            plus[m] = True
            multi[m]= multi[a] or multi[b]
        else:
            sa = dp[a]
            if plus[a]:
                sa = '(' + sa + ')'
            sb = dp[b]
            if plus[b] or multi[b]:
                sb = '(' + sb + ')'
            dp[m]   = sa + '*' + sb
            flag[m] = False
            plus[m] = plus[a] or plus[b]
            multi[m]= True

print(dp[n])
