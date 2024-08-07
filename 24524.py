import sys
input = sys.stdin.readline 

s1 = list(map(str, input().rstrip()))
s2 = list(map(str, input().rstrip()))

dp = [0]*(len(s2)+1)
dp[0] = float("inf")
find_idx = {a:idx+1 for idx,a in enumerate(s2)}

for s in s1:
    if s in find_idx and dp[find_idx[s]-1] > dp[find_idx[s]]:
        dp[find_idx[s]] += 1

print(dp[-1])