import sys
input = sys.stdin.readline

d = {}

n = int(input())
li = list(map(int, input().split()))

for i in li:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

m = int(input())
li2 = list(map(int, input().split()))

for i in li2:
    if i not in d:
        print(0, end=" ")
    else:
        print(d[i], end=" ")