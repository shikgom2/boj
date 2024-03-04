import sys
input = sys.stdin.readline
n = int(input())
d = []

for k in range(n):
    i, j = map(str, input().split())
    d.append((int(i), j, k))
d = sorted(d, key=lambda element: (element[0], element[2]))

for i in d:
    print(f"{i[0]} {i[1]}")