import sys
input = sys.stdin.readline

n = int(input())
b = bin(n)[2:]
rev = b[::-1]
ans = int(rev, 2)
print(ans)
