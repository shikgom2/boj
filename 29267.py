n, k = map(int, input().split())

save = 0
ans = 0
for _ in range(n):
    o = input()
    if o == "save":
        save = ans
    elif o == "load":
        ans = save
    elif o == "shoot":
        ans -= 1
    else:
        ans += k
    print(ans)