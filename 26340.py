n = int(input())
for _ in range(n):
    a, b, f = map(int, input().split())
    print(f"Data set: {a} {b} {f}")

    for __ in range(f):
        if a > b:
            a = a // 2
        else:
            b = b // 2
    if a > b:
        print(a, b)
    else:
        print(b, a)
    print()