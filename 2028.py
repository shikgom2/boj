import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = input().strip()
    num = int(n)
    s = str(num * num)
    if s.endswith(n):
        print("YES")
    else:
        print("NO")