import sys
input = sys.stdin.readline

n,m = map(int, input().split())
li = []
for _ in range(n):
    s = list(map(str, input().rstrip()))
    li.append(s)

