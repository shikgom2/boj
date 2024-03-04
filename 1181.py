import sys
N = int(input())

li = []
for _ in range(N):
    li.append(input())

s = sorted(set(li), key=lambda x: (len(x), x))
for i in s:
    print(i)