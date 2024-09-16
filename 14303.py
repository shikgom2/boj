import sys
input = sys.stdin.readline
MOD = 10**9+7


t = int(input())

for ttt in range(1, t + 1):
    n,m = map(int, input().split())
    
    mp = {}
    
    for _ in range(n):
        s = input().strip()
        a = [0] * 26
        for char in s:
            a[ord(char) - ord('a')] += 1
        a_tuple = tuple(a)
        if a_tuple in mp:
            mp[a_tuple] += 1
        else:
            mp[a_tuple] = 1

    ans = []
    for _ in range(m):
        s = input().strip()
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        for j in range(len(s)):
            a = [0] * 26
            for k in range(20):
                if j - k < 0:
                    break
                a[ord(s[j - k]) - ord('a')] += 1
                a_tuple = tuple(a)
                if a_tuple in mp:
                    dp[j + 1] = (dp[j + 1] + dp[j - k] * mp[a_tuple]) % MOD
        
        ans.append(dp[len(s)])

    print(f"Case #{ttt}:", end=" ")
    for i in range(len(ans)):
        print(ans[i], end=" ")
    
    print()