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

#Get prime
n = 2001
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1

N = int(input())
li = list(map(int, input().split()))

V = 2001
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)
         
odd = []
even = []

if(li[0] % 2):
    flag = 0
else:
    flag = 1 #even

for i in range(len(li)):
    #지금 코드가 odd 기준이니까... 첫수가 짝, 홀일때 그에맞게
    if(flag):
        if(li[i] % 2 == 0):
            odd.append(li[i])
        else:
            even.append(li[i])
    else:
        if(li[i] % 2 == 0):
            even.append(li[i])
        else:
            odd.append(li[i])


for i in range(len(odd)):
    for j in range(len(even)):
        if(array[odd[i] + even[j]]):
            graph[i+1].append(j+1)
print(graph)

ans = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

