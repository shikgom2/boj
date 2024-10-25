import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    ans = -1
    # (2, 3, 6)
    if n % 6 == 0:
        x = n // 2
        y = n // 3
        z = n // 6
        product = x * y * z
        if product > ans:
            ans = product
    # (2, 4, 4)
    if n % 4 == 0:
        x = n // 2
        y = n // 4
        z = n // 4
        product = x * y * z
        if product > ans:
            ans = product
    # (3, 3, 3)
    if n % 3 == 0:
        x = n // 3
        y = n // 3
        z = n // 3
        product = x * y * z
        if product > ans:
            ans = product
    print(ans)
