import sys
input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    k = int(input())
    li.append(k)

li.sort()

for i in range(len(li)):
    print(li[i])