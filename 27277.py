import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)

ans = li[0]
del li[0]

#6 1 5 2 4 3

for i in range(n//2):
    ans += (li[i] - li[n-i-2])
print(ans)