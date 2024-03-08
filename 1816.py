T = int(input())

for _ in range(T):
    num = int(input())
    i = 2
    res = True
    while i <= (10**6):
        if num % i == 0:
            res = False
            break
        i += 1

    if res:
        print("YES")
    else:
        print("NO")