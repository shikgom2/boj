n,m,k = map(int, input().split())

if n % (k-m) == 0:
    print(n // (k-m))
else:
    print(n // (k-m) + 1)