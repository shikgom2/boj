import sys
input = sys.stdin.readline

check = [[0] * 120 for _ in range(120)]

n = int(input())
ans = 0
for _ in range(n):
    a,b =map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            if not (check[i][j]):
                check[i][j] = 1
                ans += 1
        
print(ans)