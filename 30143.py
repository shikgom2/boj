n = int(input())
for _ in range(n):
    n,a,d = map(int, input().split())
    print(n*(2*a +(n-1) * d) // 2)