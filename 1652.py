import sys
input = sys.stdin.readline


N = int(input())
li = [input().strip() for _ in range(N)]

ans1 = 0
for row in li:
    length = 0
    for char in row:
        if char == '.':
            length += 1
        else:
            if length >= 2:
                ans1 += 1
            length = 0
    if length >= 2:
        ans1 += 1

ans2 = 0
for col in range(N):
    length = 0
    for row in range(N):
        if li[row][col] == '.':
            length += 1
        else:
            if length >= 2:
                ans2 += 1
            length = 0
    if length >= 2:
        ans2 += 1

print(ans1, ans2)
