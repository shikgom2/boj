import sys
input = sys.stdin.readline 

def dp(A_std, A_ult, B_std, B_ult, st, ut):
    if A_std + A_ult + B_std + B_ult == 0:
        return 0
    
    key = (A_std, A_ult, B_std, B_ult, st, ut)
    if key in memo:
        return memo[key]
    
    p = T_total - (A_std + A_ult + B_std + B_ult)
    cur = li[p]
    
    if cur <= n:
        best = -10**15
        if A_std > 0:
            best = max(best, li2[st] + dp(A_std - 1, A_ult, B_std, B_ult, st + 1, ut))
        if A_ult > 0:
            best = max(best, li3[ut] + dp(A_std, A_ult - 1, B_std, B_ult, st, ut + 1))
        memo[key] = best
    else:
        best = 10**15
        if B_std > 0:
            best = min(best, -li2[st] + dp(A_std, A_ult, B_std - 1, B_ult, st + 1, ut))
        if B_ult > 0:
            best = min(best, -li3[ut] + dp(A_std, A_ult, B_std, B_ult - 1, st, ut + 1))
        memo[key] = best
    
    return memo[key]

n, s = map(int, input().split())
T = 2 * n * (s + 1)

li = list(map(int, input().split()))

p_s = int(input())
li2 = list(map(int, input().split()))

p_u = int(input())
li3 = list(map(int, input().split()))

li2.sort(reverse=True)
li3.sort(reverse=True)

T_total = T
memo = {}
print(dp(n * s, n, n * s, n, 0, 0))
