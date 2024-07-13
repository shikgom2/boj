import sys
input = sys.stdin.readline

n,m = map(int, input().split())

li = []
for _ in range(n):
	s = list(map(str, input().rstrip()))
	li.append(s)

dp = [0 for _ in range(n+1)]
dp[n] = 1
for j in range(m):
	ndp = [0 for __ in range(n+1)]

	big = 0
	for i in range(n):
		if(li[i][j] == 'B'):
			big = i+1
	small = n
	for i in range(n-1,-1,-1):
		if(li[i][j] == 'R'):
			small = i

	for i in range(n,-1,-1):
		if i<n:
			dp[i] += dp[i+1]
		if(i >= big and i <= small):
			ndp[i] = dp[i]
	dp = ndp

print(sum(dp))