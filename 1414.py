import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

def char_to_number(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 27
    elif c == '0':
        return 0
    
n = int(input())

graph = []
parent = [i for i in range(n + 1)]

total = 0
for i in range(n):
    li = list(map(str, input().rstrip()))
    for j in range(len(li)):
        if(li[j] != '0'):
            weight = char_to_number(li[j])
            if(i != j):
                graph.append((i, j, weight))
                
            total += weight
            
graph.sort(key=lambda x:x[2])
ans = 0
count = 0
for i in range(len(graph)):
    x = graph[i][0]
    y = graph[i][1]
    z = graph[i][2]
    if find(x) != find(y):
        union(x, y)
        ans = ans + z
        count += 1
        
if(count != n-1):
    print(-1)
else:
    print(total - ans)