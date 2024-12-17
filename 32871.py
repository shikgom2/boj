import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if min(n,m) %2 == 1:
        print("YES")
    else:
        print("NO")