import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0

    for _ in range(n):
        a,b,c = map(int, input().split())
        ans += max(0, a,b,c)

    print(ans)