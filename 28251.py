import sys
input = sys.stdin.readline 

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    
    if(a > b):
        parent[a] = b 
        power[b] += li[a] * li[b] +power[a]
        li[b] += li[a]
    elif(a<b):
        parent[b] = a
        power[a] += li[b] * li[a] + power[b]
        li[a] += li[b] 
        
n,m = map(int, input().split())
li = [0] + list(map(int, input().split()))

parent = [i for i in range(n + 1)]

power = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    if(find(a) != find(b)):
        union(a,b)
    print(power[find(a)])