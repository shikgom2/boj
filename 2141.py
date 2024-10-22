import sys
input = sys.stdin.readline
 
n = int(input())
prefix = 0
li = []
for _ in range(n):
    a,b = map(int, input().split())
    prefix += b
    li.append((a,b))

#li.sort()
cur = 0
idx = 0
while(cur < prefix / 2):
    cur += li[idx][1]
    idx += 1
    
print(li[idx-1][0]) 