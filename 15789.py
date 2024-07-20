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

n,m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    a,b = map(int, input().split())
    union(a,b)

a, b, k = map(int, input().split()) 

li1 = [] #enemy
li2 = [] #our

for i in range(1, n):
    if(find(i) == find(b)):
        li1.append(i)
    elif(find(i) == find(a)):
        li2.append(i)

for i in range(len(li1)):
    parent[li1[i]] = 0

for i in range(len(li2)):
    parent[li2[i]] = 0

check = [0] * (100001)
for i in range(1, len(parent)):
    if(parent[i] != 0):
        check[parent[i]] += 1

check.sort(reverse=True)

ans = len(li2)
for i in range(k):
    ans += check[i]
print(ans)