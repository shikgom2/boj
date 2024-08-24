import sys
input = sys.stdin.readline

n = int(input())
ans  = 1
num = 1
cur = 0
while(n > num):
    cur += 6
    num += cur
    ans += 1
print(ans)