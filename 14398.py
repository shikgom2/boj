import sys
input = sys.stdin.readline
import math

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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def test(n):
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n

V = 2001
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n = int(input())

li = list(map(int, input().split()))

odd = []
even = []
for i in range(len(li)):
    if(li[i] % 2 == 0):
        even.append(li[i])
    else:
        odd.append(li[i])

graph = [[] for _ in range(n+1)]

for i in range(len(odd)):
    for j in range(len(even)):
        if(gcd(odd[i], even[j]) == 1 and test(odd[i]**2 + even[j]**2)):
            graph[i].append(j)

ans = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    ans += dfs(i)

print(ans)