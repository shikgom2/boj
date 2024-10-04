import sys
input = sys.stdin.readline


li = []
for _ in range(10):
    k = int(input())
    li.append(k)

prefix = [0] * 10
prefix[0] = li[0]

for i in range(1, 10):
    prefix[i] = prefix[i-1] + li[i]

ans = 10**10

for i in range(10):
    if(abs(prefix[i] - 100) <= abs(ans - 100)):
        ans = prefix[i]

print(ans)