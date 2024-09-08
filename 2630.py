import sys
input = sys.stdin.readline

def check(row,col,n):
    global blue, white

    cur = li[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if cur != li[i][j]:
                next_n = n // 2
                check(row, col, next_n)
                check(row, col + next_n, next_n)
                check(row + next_n, col, next_n)
                check(row + next_n, col + next_n, next_n)
                return
    if cur == 0:
        white += 1
    else:
        blue += 1
    return

n = int(input())
li = []

for _ in range(n):
    a = list(map(int,input().rsplit()))
    li.append(a)

blue, white = 0, 0

check(0,0,n)
print(white)
print(blue)