import sys
input = sys.stdin.readline

n,m = map(int, input().split())

mod = 10**9 + 7

q = n*m//3

if(n*m == 1):
    print(1)
    exit()
elif((n*m)%3 == 0):
    ans = 3 ** q % mod
elif((n*m)%3 == 1):
    ans = 3 ** (q-1) * 4 % mod
elif((n*m)%3 == 2):
    ans = 3 ** q * 2 % mod

print(ans)