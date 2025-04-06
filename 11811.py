import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in range(n):
    a = 0
    for j in range(n):
        if i != j:
            a |= li[i][j]
    ans.append(a)
print(" ".join(map(str, ans)))