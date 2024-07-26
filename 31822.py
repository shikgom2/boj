li = input()[:5]
n = int(input())
ans = 0
for _ in range(n):
    s = input()
    if s[:5] == li:
        ans += 1
print(ans)