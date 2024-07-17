import sys
input = sys.stdin.readline

check = [[False for _ in range(100)] for _ in range(100)]

ans = 0
for _ in range(4):
    a, b, c, d =map(int, input().split())

    for i in range(a, c):
        for j in range(b, d):
            if(check[i][j] == False):
                check[i][j] = True
                ans += 1

print(ans)