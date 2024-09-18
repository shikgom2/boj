import sys
inptut = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n):
    start = i
    tmp = str(start)
    print(tmp)
    for k in tmp:
        print(i ,":" , k)
        start += int(k)
    if start <= n:
        dp[start] = 1

print(dp[n])
