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

n = int(input())
parent = [i for i in range(n + 1)]

for _ in range(n-2):
    a, b = map(int, input().split())
    union(a, b)
    
for i in range(2, n+1):
    if(find(1) != find(i)):
        print(1, i)
        break