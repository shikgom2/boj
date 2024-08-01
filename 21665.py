import sys
input = sys.stdin.readline
n, m = map(int, input().split())

ori = []
rev = []

for i in range(n):
    li = input()
    ori.append(li)

next_line = input()
for i in range(n):
    li = input()
    rev.append(li)

ans = 0
for i in range(n):
    for j in range(m):
        if ori[i][j] == rev[i][j]:
            ans += 1
print(ans)