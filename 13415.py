import sys
input = sys.stdin.readline

i=int(input())
li = list(map(int, input().split()))

n=int(input())

max_i = 0
max_j = 0
last_i = 0
last_j = 0
for k in range(n):
    i,j = map(int, input().split())
    if(k == n-1):
        last_i = i
        last_j = j

    max_i = max(i, max_i)
    max_j = max(j, max_j)

li[:max_i] = sorted(li[:max_i])
li[:max_j] = sorted(li[:max_j], reverse=True)

li[:last_i] = sorted(li[:last_i])
li[:last_j] = sorted(li[:last_j], reverse=True)

print(*li)