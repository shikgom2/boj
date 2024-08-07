import sys
input = sys.stdin.readline 

n = int(input())
li = list(map(int, input().split()))

li.sort(reverse=True)
ans = 0
for i in range(1, len(li)):
    ans += (li[i] / 2)

print(li[0] + ans)