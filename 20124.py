import sys
input = sys.stdin.readline 

li = []
n = int(input()) 
for _ in range(n):
    l = list(map(str, input().split()))
    li.append((l[0], int(l[1])))

li.sort(key= lambda x : (-x[1], x[0]))

print(li[0][0])