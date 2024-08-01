n, m = map(int, input().split())

ans = 0
for _ in range(n):
    s = input()
    for i in s:
        if i == "+":
            ans += 1
            break
print(ans)