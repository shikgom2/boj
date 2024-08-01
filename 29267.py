n, k = map(int, input().split())

save = 0
cur = 0
for _ in range(n):
    o = input()
    if o == "save":
        save = cur
    elif o == "load":
        cur = save
    elif o == "shoot":
        cur -= 1
    else:
        cur += k
    print(cur)