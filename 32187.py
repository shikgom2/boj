import sys
input = sys.stdin.readline

def solve(use):
    dp = [0, 0]
    
    for i in range(len(use)):
        ndp = [0, 0]
        ndp[0] = max(dp[0], dp[1])
        ndp[1] = max(dp[1], dp[0] + use[i][1])
        
        if i == 0 or use[i][0] != use[i - 1][0] + 1:
            ndp[1] = max(ndp[1], dp[1] + use[i][1])
        
        dp = ndp
    
    return max(dp)

n,m = map(int, input().split())

use = [[] for _ in range(n+1)]
for i in range(m):
    arr = list(map(int, input().split()))
    for j in range(1, len(arr), 2):
        id = arr[j]
        val = arr[j+1]
        use[id].append((i, val))

ans = 0
for i in range(1, n+1):
    ans += solve(use[i])

print(ans)
