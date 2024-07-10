import sys
input = sys.stdin.readline

def dfs(x):
    global visited, even, odd

    visited.add(x)
    for b in graph[x]:
        if even[b] == -1 or ((even[b] not in visited) and dfs(even[b])):
            odd[x] = b
            even[b] = x
            return True

    return False

t = int(input())
for _ in range(t):
    V = 10001
    graph = [[] for _ in range(V+1)]
    d = [0] * (V+1)

    n, m = map(int, input().split())
    li = []

    for _ in range(n):
        s = list(map(str, input().rstrip()))
        li.append(s)

    even = [-1] * (n * m)
    odd = [-1] * (n * m)
    total = 0


    di = [[-1, -1], [0, -1], [1, -1], [-1, 1], [0, 1], [1, 1]]
    for j in range(m):
        for i in range(n):
            if li[i][j] == 'x':
                continue

            total += 1

            if j & 1:
                continue

            for dy, dx in di:
                ty = i + dy
                tx = j + dx
                if 0 <= ty < n and 0 <= tx < m and li[ty][tx] == '.':
                    graph[i * m + j].append(ty * m + tx)

    '''
    #2dim -> 1dim, (k-1), (k+1), (k-m-1), (k-m+1), x되어있는 곳은 이분그래프 연결 x
    li = [item for sublist in li for item in sublist]
    
    for i in range(len(li)):
        for j in range(len(li)):
            #left
            if(i % m != 1 and j == max(0, i-1)):
                continue
            #right
            elif(i % m != 0 and j == i+1):
                continue
            #digonical
            elif(j == max(0, i-m-1)):
                continue
            elif(j == max(0, i-m+1)):
                continue
            elif(li[j] == 'x'):
                continue
            elif(i == j):
                continue
            else:
                graph[i+1].append(j+1)
    print(graph)
    '''
    ans = 0

    for j in range(0, m, 2):
        for i in range(n):
            visited = set()
            if dfs(i * m + j):
                ans += 1

    print(total - ans)