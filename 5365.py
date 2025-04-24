import sys
input = sys.stdin.readline

n = int(input())
li = []
while len(li) < n:
    li += input().split()

ans = []
ans.append(li[0][0])

for i in range(1, n):
    prev = len(li[i-1])
    if prev <= len(li[i]):
        ans.append(li[i][prev-1])
    else:
        ans.append(' ')

print(''.join(ans))
