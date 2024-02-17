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

edges = []
parent = [i for i in range(n + 1)]
ans = 0
sum = 0

for i in range(0, n):
    weights = list(map(str, input().strip()))

    for j in range(len(weights)):
        weight = char_to_number(weights[j])
        sum += weight
        edges.append((weight, i, j))

edges.sort()

for edge in edges:
    z, x, y = edge
    if find(x) != find(y):
        union(x, y)
        ans += z

connected = True
root = find(0)
for i in range(1, n):
    if find(i) != root:
        connected = False
        break

if(connected):
    print(sum - ans)
else:
    print(-1)