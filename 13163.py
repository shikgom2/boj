import sys
input = sys.stdin.readline


n = int(input())
for _ in range(n):
    li = list(map(str, input().split()))
    li[0] = 'god'
    print(*li, sep="")