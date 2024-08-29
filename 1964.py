import sys
input = sys.stdin.readline 

n = int(input())
# 5 12 22 
ans = 5
update = 4
mod = 45678
for i in range(1, n):
    update += 3
    ans = (ans + update) % mod
print(ans)