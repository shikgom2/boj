while True:
    b, n = map(int, input().split())

    if b == 0 and n == 0:
        break

    if n == 1:
        ans = b
    else:
        a = 1
        while (a + 1) ** n <= b:
            a += 1
        diff1 = b - a ** n
        diff2 = (a + 1) ** n - b
        if diff1 <= diff2:
            ans = a
        else:
            ans = a + 1

    print(ans)
