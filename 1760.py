import sys
input = sys.stdin.readline

def dfs(x):
    for i in range(len(graph[x])):
        t = graph[x][i]
        if c[t]:
            continue
        c[t] = True
        if d[t] == 0 or dfs(d[t]):
            d[t] = x
            return True
    return False

V = 101
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n, m = map(int, input().split())




board = [[] for _ in range(n)]
idx = 1
for i in range(n):
    li = list(map(int, input().split()))
    for j in range(len(li)):
        if(li[j] == 0):
            board[i].append(idx)
        elif(li[j] == 1):
            board[i].append(0)
        elif(li[j] == 2):
            idx += 1
            board[i].append(0)
print(board)


for i in range(n):
    for j in range(m):
        if(board[i][j] != board[i][j]):
            

#print(graph)

ans = 0
for i in range(1, m + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(ans)