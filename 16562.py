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

n,m,k = map(int, input().split())
parent = [i for i in range(n + 1)]

money = list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    union(a,b)

li = [[] for _ in range(n+1)]

for i in range(1, n+1):
    res = find(i)
    li[res].append(money[i-1])

ans = 0
for i in range(len(li)):
    if(len(li[i])):
        ans = ans + min(li[i])

if(ans <= k):
    print(ans)
else:
    print("Oh no")