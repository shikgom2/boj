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

def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)


while(True):
    V = 1001
    graph = [[] for _ in range(V+1)]
    d = [0] * (V+1)

    n, m = map(int, input().split())
    if(n==0 and m == 0):
        break
    li = []
    li1 = []
    
    k = n//10
    if(n%10 != 0):
        k+=1
    for _ in range(k):
        tmp = list(map(int, input().split()))
        for i in tmp:
            li.append(i)
            
    k = m//10
    if(m%10 != 0):
        k+=1
    for _ in range(k):
        tmp = list(map(int, input().split()))
        for i in tmp:
            li1.append(i)
    
    
    for i in range(len(li)):
        for j in range(len(li1)):
            if(gcd(li[i], li1[j]) > 1):
                graph[i+1].append(j+1)
                
    ans = 0
    for i in range(1, n + 1):
        c = [False] * (V+1)
        if dfs(i):
            ans += 1

    print(ans)