import sys
input = sys.stdin.readline 

X, Y = map(int, input().split())
N = int(input())

ans = X / Y

for _ in range(N):
    Xi, Yi = map(int, input().split())
    price_per_gram = Xi / Yi
    if price_per_gram < ans:
        ans = price_per_gram

print(f"{ ans * 1000:.2f}")
