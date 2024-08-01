n,m = map(int, input().split())
ans = 0
for _ in range(N):
    s = input()
    yes = 0
    no = 0
    for i in s:
        if i == "O":
            yes += 1
        else:
            no += 1
    if yes > no:
        ans += 1
print(ans)