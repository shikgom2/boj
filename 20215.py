w, h = map(int, input().split())
ans = w + h - (w**2 + h**2) ** (1 / 2)
print(ans)