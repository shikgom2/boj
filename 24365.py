li = list(map(int, input().split()))
ans = sum(li) // 3
print((ans - li[0]) * 2 + ans - li[1])