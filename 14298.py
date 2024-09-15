t = int(input())
for x in range(1, t + 1):
    n,m = map(int, input().split())
    print(f"Case #{x}: {(n-m) / (n + m)}")