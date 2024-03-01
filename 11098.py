import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    k = int(input())
    li = []
    for _ in range(k):
        i, j = map(str, input().split())
        li.append((int(i), j))

        li.sort(reverse=True)
    print(li[0][1])