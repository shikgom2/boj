import sys
input = sys.stdin.readline

n, a, b, c, d = map(int, input().split())

A_set = n // a
if n % a != 0:
    A_set += 1
C_set = n // c
if n % c != 0:
    C_set += 1
print(min(A_set * b, C_set * d))