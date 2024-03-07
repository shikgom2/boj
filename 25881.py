a, b = map(int, input().split())
n = int(input())

for _ in range(n):
    k = int(input())
    if k > 1000:
        print(k, a * 1000 + b * (k - 1000))
    else:
        print(k, k * a)