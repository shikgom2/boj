import sys
input = sys.stdin.readline

def dfs2(u, path, b, check2, sum_val):
    if not check2[path[u]]:
        check2[path[u]] = True
        sum_val[0] *= b[u][path[u]]
        dfs2(path[u], path, b, check2, sum_val)

def dfs(u, n, b, check, path, min1, max1):
    if u == n:
        check2 = [False] * n
        c = 0
        sum_val = [1]
        for i in range(n):
            if not check2[path[i]]:
                c += 1
                check2[path[i]] = True
                sum_val[0] *= b[i][path[i]]
                dfs2(path[i], path, b, check2, sum_val)
        
        if c % 2 == 0:
            sum_val[0] *= -1
        min1[0] = min(min1[0], sum_val[0])
        max1[0] = max(max1[0], sum_val[0])
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            path[u] = i
            dfs(u + 1, n, b, check, path, min1, max1)
            check[i] = False

n = int(input())
board = []
for _ in range(n):
    li = list(map(str, input().rstrip()))
    board.append(li)

b = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if '0' <= board[i][j] <= '9':
            b[i][j] = int(board[i][j])
        else:
            b[i][j] = -1 * (ord(board[i][j]) - ord('A') + 1)

check = [False] * n
path = [-1] * n
min1 = [float('inf')]
max1 = [-float('inf')]

dfs(0, n, b, check, path, min1, max1)
ans = (min1[0] + max1[0])

if ans >= 0:
    print(ans % 121547)
else:
    print(121547 + ans)
