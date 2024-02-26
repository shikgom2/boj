import sys
input = sys.stdin.readline

def near(x):
    ret = -1
    minIdx = -1
    for i in range(n):
        if isSpecial[i] == 0:
            continue
        if ret == -1 or ret > dist[x][i]:
            ret = dist[x][i]
            minIdx = i
    return minIdx

def findTheLength(a, b):
    directLength = dist[a][b]
    if isSpecial[a] == 1 and isSpecial[b] == 1:
        directLength = min(directLength, t)
    
    nearA = near(a)
    nearB = near(b)
    
    if nearA != -1 and nearB != -1:
        directLength = min(directLength, dist[a][nearA] + t + dist[nearB][b])
    
    return directLength

n, t = map(int, input().split())

x = [0] * 1000
y = [0] * 1000
isSpecial = [0] * 1000
dist = [[0] * 1001 for _ in range(1001)]

for i in range(n):
    isSpecial[i], x[i], y[i] = map(int, input().split())

for i in range(n):
    for j in range(i + 1, n):
        dist[i][j] = dist[j][i] = abs(x[i] - x[j]) + abs(y[i] - y[j])

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(findTheLength(a, b))