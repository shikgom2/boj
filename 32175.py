import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
mod = 10**9 + 7

def solve(coins, h, memo=None):
    if memo is None:
        memo = {}
    
    if h in memo:
        return memo[h]
    
    if h == 0:
        return 1
    if h < 0:
        return 0
    
    count = 0
    for coin in coins:
        count += solve(coins, h - coin, memo)
        count %= mod
    
    memo[h] = count
    return count

n,m = map(int, input().split())
li = list(map(int, input().split()))
print(solve(li, m))