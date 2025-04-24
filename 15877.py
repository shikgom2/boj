import sys
input = sys.stdin.readline

a, b = map(int, input().split())
dp = [[False] * (b+1) for _ in range(a+1)]

mov = [(1,0), (0,1), (3,1), (1,3)]
for i in range(a+1):
    for j in range(b+1):
        if i == 0 and j == 0:
            continue
        
        flag = False
        for di, dj in mov:
            ni = i - di
            nj = j - dj
            
            if ni >= 0 and nj >= 0 and not dp[ni][nj]:
                flag = True
                break
        dp[i][j] = flag

if dp[a][b]:
    print("Alice")
else:
    print("Bob")