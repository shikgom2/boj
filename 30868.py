t = int(input())
for _ in range(t):
    n = int(input())
    ans = ["++++" for _ in range(n // 5)]
    ans.append("|" * (n % 5))
    print(*ans)