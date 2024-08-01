n = int(input())

for _ in range(n):
    x = int(input())
    res = 0
    for _ in range(x):
        pr, a, p = input().split()
        res += float(a) * float(p)
    ans = round(res, 2)
    print("${:.2f}".format(ans))