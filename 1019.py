n = int(input())
cnt = [0 for _ in range(10)]
add = 0
i = 1

while n != 0:
    cur = n % 10
    n //= 10

    cnt[0] -= i
    for j in range(0, cur):
        cnt[j] += (n + 1) * i
    cnt[cur] += n * i + 1 + add
    for j in range(cur + 1, 10):
        cnt[j] += n * i

    add += cur * i
    i *= 10

for i in range(10):
    print(cnt[i], end=" ")