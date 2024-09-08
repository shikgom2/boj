import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,e = map(int, input().split())

    for i in range(2, 1001):
        if (n % i == 0):
            p = i
            q = n // i
            break

    phi = (p-1) * (q-1)
    for i in range(1, phi):
        if (e * i % phi == 1):
            print(i)
            break
