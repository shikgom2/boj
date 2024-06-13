n,m = map(int, input().split())
k = int(input())
n = n+m
if (k*2 <= n):
    print(n - k*2)
else:
    print(n)