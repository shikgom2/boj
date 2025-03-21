import sys
input = sys.stdin.readline

def recur(n):
    if n < 10:
        memo = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]
        return memo[n]
    else:     
        return (recur(n // 5) * recur(n % 5) * pow(2, n // 5, 10)) % 10

n = int(input())
print(recur(n))
