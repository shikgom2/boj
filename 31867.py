import sys
input = sys.stdin.readline
N = int(input())
K = input()
ans = 0
for i in K:
    if int(i) % 2 == 0:
        ans += 1
    else:
        ans -= 1
if ans == 0:
    print(-1)
elif ans > 0:
    print(0)
else:
    print(1)