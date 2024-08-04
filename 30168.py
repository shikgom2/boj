import sys
input = sys.stdin.readline

mat = [[0] * 1001 for _ in range(1001)]
n, m = map(int, input().split())

ans = 1
for i in range(n):
    x = int(input().strip())
    for j in range(x):
        mat[i][j] = 1
    mat[i][x] = -1

for j in range(m):
    x = int(input().strip())
    for i in range(x):
        if mat[i][j] == -1:
            ans = 0
        mat[i][j] = 1

    if mat[x][j] == 1:
        ans = 0
    mat[x][j] = -1

MOD = 10**9 + 7
for i in range(n):
    for j in range(m):
        if li[i][j] == 0:
            ans = (ans * 2) % MOD

print(ans)