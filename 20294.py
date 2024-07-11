import math
import sys
input = sys.stdin.readline

def distance_3d(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return dist

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

V = 10001
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n = int(input())

group1 = []
group2 = []

for _ in range(n):
    x,y,z = map(int, input().split())
    if((abs(x) + abs(y) + abs(z)) % 2):
        group2.append((x,y,z)) #odd
    else:
        group1.append((x,y,z)) #even

#print(group1)
#print(group2)

for i in range(len(group1)):
    for j in range(len(group2)):
        dist = distance_3d(group1[i], group2[j])
        if(dist <= 1):
            #print(f"{group1[i]} -> {group2[j]} dist : {dist}")
            graph[i+1].append(j+1)

ans = 0

for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

#print(ans) #최대 매칭

ans1 = 0
check = [False] * (len(group2) + 1)

for i in range(1, len(group1)+1):
    if(len(graph[i]) == 0):
        ans1 += 1 #group1에서 매칭이 안된거
    else:
        for j in range(len(graph[i])):
            idx = graph[i][j]
            check[idx] = True

ans2 = 0

for i in range( 1,len(check)): #group2에서 매칭안된거
    if not check[i]:
        ans2 += 1

print(ans + ans1 + ans2)