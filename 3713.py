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

V = 10000
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)
dddd=0
t = int(input())
for _ in range(t):
    V = 501
    graph = [[] for _ in range(V+1)]
    d = [0] * (V+1)

    n = int(input())
    height = []
    gender = []
    music = []
    sports = []
    for _ in range(n):
        li = list(map(str, input().split()))
        height.append(int(li[0]))
        gender.append(li[1])
        music.append(li[2])
        sports.append(li[3])
    
    for i in range(n):
        for j in range(n):
            if(i == j):
                dddd=0
            elif((abs(height[i] - height[j]) < 40) and
                 (gender[i] != gender[j]) and
                 (music[i] == music[j]) and
                 (sports[i] != sports[j])):
                graph[i+1].append(j+1)
    
    print(graph)
    
    ans = 0
    for i in graph:
        ans = max(ans, len(i))
    print(ans)
    '''
    ans = 0
    for i in range(1, n+ 1):
        c = [False] * (V+1)
        if dfs(i):
            ans += 1

    print(ans)
    '''