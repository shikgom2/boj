import sys
input = sys.stdin.readline

n = int(input())
d = 2
for _ in range(n):
    d += (d-1)
print(d*d)