import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    x, y = map(int, input().split())
    li.append((x, y))

li.sort(key=lambda x: (x[1], x[0]))
for i,j in li:
    print(f"{i} {j}")
