t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    dp = [[0] * n for i in range(n)]

