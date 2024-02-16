import sys
input = sys.stdin.readline
N = int(input())

point = []
for i in range(N):
    a,b = map(int, input().split())
    point.append((a,b))

point.sort()

for p in point:
    print(p[0], p[1])