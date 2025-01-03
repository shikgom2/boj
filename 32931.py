import sys
input = sys.stdin.readline

n = int(input()[0])
top_row = list(map(int, input().split()))
bot_row = list(map(int, input().split()))

# dp[i][0] = i번 열, 위 행에 도달했을 때의 최대합
# dp[i][1] = i번 열, 아래 행에 도달했을 때의 최대합
INF_NEG = float('-inf')
dp = [[-10**10, -10**10] for _ in range(n )]

# 초기화
dp[0][0] = top_row[0]
dp[0][1] = top_row[0] + bot_row[0]

for i in range(1, n):
    t = top_row[i]
    b = bot_row[i]
    # 위 행으로 i번째 열에 도달
    dp[i][0] = max(dp[i-1][0] + t,   # 위->위 수평이동
                    dp[i-1][1] + t + b)  # 아래->위 교차
    # 아래 행으로 i번째 열에 도달
    dp[i][1] = max(dp[i-1][1] + b,   # 아래->아래 수평이동
                    dp[i-1][0] + t + b) # 위->아래 교차

ans = max(dp[n -1][0], dp[n -1][1])
print(ans)
