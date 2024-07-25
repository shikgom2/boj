t = int(input())

for _ in range(t):
    ans = 0
    s = input()
    for i in s:
        if i == "U":
            ans += 1
        else:
            break
    print(ans)