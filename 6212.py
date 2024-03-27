M, N = map(int, input().split())
cnt = [0] * 10
for i in range(M, N + 1):
    n = i
    while n:
        cnt[n % 10] += 1
        n //= 10
for i in cnt:
    print(i, end=' ')