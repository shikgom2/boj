import sys
input = sys.stdin.readline

n,k = map(int, input().split())
li = []

for _ in range(n):
    s = list(map(str,input().rstrip()))
    li.append(s)
li.sort()
print(*li[k-1], sep="")