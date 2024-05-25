import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#x, y, count(탐색한 알파벳 수)
def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #탐색 조건
        if(0<=nx<r and 0<=ny<c and visited[ord(li[nx][ny])-ord('A')]==0):
            #set visited
            visited[ord(li[nx][ny]) - 65] = 1
            # next index
            dfs(nx, ny, count+1)
            # for next visited index
            visited[ord(li[nx][ny]) - 65] = 0

#input
r, c = map(int, input().split())
li = []
for _ in range(r):
    s = input().rstrip()
    li.append(s)

ans = 0
visited=[0] * 26

#왼쪽 최상단 먼저 탐색 시작이니, 여기부터 시작
visited[ord(li[0][0]) - 65] = 1
#x, y, count(탐색한 알파벳 수)
dfs(0, 0, 1)
print(ans)