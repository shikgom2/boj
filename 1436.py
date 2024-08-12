import sys
input = sys.stdin.readline

n = int(input())

cur = 666
cnt = 0
while(True):
    s = str(cur)
    if("666" in s):
        cnt += 1
    
    if(cnt == n):
        break
    cur += 1
print(cur)