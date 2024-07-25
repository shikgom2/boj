import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    n = int(input())
    print(f"{n} is odd" if n%2 else f"{n} is even")