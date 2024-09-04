import sys
input = sys.stdin.readline

li = []
n = int(input())
for _ in range(n):
    s,c,l =map(int, input().split())
    li.append((s,c,l))

li2 = li.copy()
li2.sort(key=lambda x : (-x[0], x[1], x[2]))

print(li.index(li2[0]) + 1)