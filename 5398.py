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

t = int(input())
for _ in range(t):
    V = 2020
    graph = [[] for _ in range(V+1)]
    d = [0] * (V+1)

    n, m = map(int, input().split())
    maps = [["0" for _ in range(V+1)] for _ in range(V+1)]
    
    for a in range(n):
        x,y,s = map(str, input().split())
        x = int(x)
        y = int(y)
        for i in range(len(s)):
            maps[y][x] = (s[i], a)
            x += 1

    #print(maps)

    for a in range(m):
        x,y,s = map(str, input().split())
        x = int(x)
        y = int(y)
        #세로로 삽입하고 겹치는지 확인, 겹치면 이분그래프에 삽입
        for i in range(len(s)):
            if(maps[y][x] == '0'):
                maps[y][x] = (s[i], a)
                #print("add ", s[i], "at ", y, ", " , x)
            #이미 가로에 단어를 작성
            elif(maps[y][x] != 0 and maps[y][x][0] != s[i]): #다르다면, 이분그래프에 작성
                idx = maps[y][x][1]
                #print("garo : ", maps[y][x][0], "sero : ", s[i], "is different!")
                graph[idx+1].append(a+1)
            '''
            elif(maps[y][x][0] == s[i]): #같다면 계속진행
                print("garo : ", maps[y][x][0], "sero : ", s[i])
            '''
            y += 1

    #print(graph)

    ans = 0
    for i in range(1, (n+m) + 1):
        c = [False] * (V+1)
        if dfs(i):
            ans += 1

    print((n+m) - ans)