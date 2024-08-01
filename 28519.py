n,m= map(int, input().split())

if n > m:
    print(2 * m + 1)
elif n < m:
    print(2 * n + 1)
else:
    print(n+m)