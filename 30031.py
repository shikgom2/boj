n = int(input())
ans = 0
for _ in range(n):
    w, h = map(int, input().split())
    if w == 136:
        ans += 1000
    elif w == 142:
        ans += 5000
    elif w == 148:
        ans += 10000
    else:
        ans += 50000
print(ans)