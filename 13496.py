import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    n, s, d = map(int, input().split())
    ans = 0
    for _ in range(n):
        di, dv = map(int, input().split())
        if s * d >= di:
            ans += dv
    print(f"Data Set {i+1}:")
    print(ans)
    if i != t + 1:
        print()