t = int(input())

for _ in range(t):
    n = int(input())
    ans = 1
    for i in range(2, n + 1):
        ans *= i

    print(ans % 10)