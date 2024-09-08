import sys
input = sys.stdin.readline

def check(row,col,n):
    global one, two ,three

    cur = li[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if cur != li[i][j]:
                next_n = n // 3
                check(row, col, next_n)
                check(row, col + next_n, next_n)
                check(row, col + (2 * next_n), next_n)
                check(row + next_n, col, next_n)
                check(row + next_n, col + next_n, next_n)
                check(row + next_n, col + (2 * next_n), next_n)
                check(row + (2 * next_n), col, next_n)
                check(row + (2 * next_n), col + next_n, next_n)
                check(row + (2 * next_n), col + (2 * next_n), next_n)
                return
    if cur == -1:
        one += 1
    elif cur == 0:
        two += 1
    elif cur == 1:
        three += 1
    return

n = int(input())
li = []

for _ in range(n):
    a = list(map(int,input().rsplit()))
    li.append(a)

one, two, three = 0,0,0

check(0, 0, n)
print(one)
print(two)
print(three)