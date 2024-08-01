n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in a:
    ans += i // k
print(ans)