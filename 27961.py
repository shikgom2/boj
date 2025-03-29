import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    exit()

k = n.bit_length() - 1

if (1 << k) == n:
    print(k + 1)
else:
    print(k + 2)
    