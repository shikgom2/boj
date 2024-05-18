n, m = map(int, input().split())
k = 1

for _ in range(n):
    for _ in range(m):
        if k % m == 0:
            print(k, end = '')
        else:
            print(k, end = ' ')
        k += 1
    print()