import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        print(i+1, x+50000000, y+1)