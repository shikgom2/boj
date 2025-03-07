import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = list(map(int, input().split()))
li = [0] + li
S = [0] * (N + 1)
S2 = [0] * (N + 1)

for i in range(1, N + 1):
    S[i] = S[i - 1] + li[i]
    S2[i] = S2[i - 1] + li[i] * li[i]
    
INF = 10**20

dp = [[(None, None) for _ in range(M + 1)] for _ in range(N + 2)]

for m in range(M + 1):
    if m == 0:
        dp[N + 1][m] = (0, [])
    else:
        dp[N + 1][m] = (INF, [])
        
for i in range(N, 0, -1):
    dp[i][0] = ( ((S[N] - S[i - 1]) * (S[N] - S[i - 1]) - (S2[N] - S2[i - 1])) // 2, [] )
    for m in range(1, M + 1):
        
        cost = INF
        seq = []
        for k in range(i, N + 1):
            s = S[k] - S[i - 1]
            s2 = S2[k] - S2[i - 1]
            seg = (s * s - s2) // 2
            can = seg + dp[k + 1][m - 1][0]
            can_seq = [k] + dp[k + 1][m - 1][1]
            if can < cost:
                cost = can
                seq = can_seq
            elif can == cost and can_seq < seq:
                seq = can_seq
        dp[i][m] = (cost, seq)
        
cost, ans = dp[1][M]
print(cost)
print(" ".join(map(str, ans)) + "\n")
