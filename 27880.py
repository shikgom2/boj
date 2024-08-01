ans = 0
for i in range(4):
    n, s = input().split()
    s = int(s)

    if n == "Es":
        ans += s * 21
    else:
        ans += s * 17

print(ans)