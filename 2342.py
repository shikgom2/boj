import sys

move = [[1, 2, 2, 2, 2],
        [3, 1, 3, 4, 3],
        [3, 3, 1, 3, 4],
        [3, 4, 3, 1, 3],
        [3, 3, 4, 3, 1]]

li = list(map(int, input().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(len(li) + 1)]

for n in range(len(li) - 1, -1, -1):
    for left in range(5):
        for right in range(5):
            if li[n] != left and li[n] != right:
                move_left = move[left][li[n]]
                move_right = move[li[n]][right]
                dp[n][left][right] = min(dp[n + 1][li[n]][right] + move_left, dp[n + 1][left][li[n]] + move_right)

res = dp[0][0][0]
print(res)