import sys
input = sys.stdin.readline


def solve():
    n, m, q = map(int, input().split())
    a_str = input().strip()
    b_str = input().strip()
    f = [0] * (n + 1)
    g = [0] * (m + 1)
    if a_str[0] == "0" or b_str[0] == "0":
        f[1] = 1
    else:
        f[1] = 0
    for i in range(2, n + 1):
        if a_str[i - 1] == "0":
            f[i] = 1
        else:
            f[i] = 1 - f[i - 1]
    g[1] = f[1]
    for j in range(2, m + 1):
        if b_str[j - 1] == "0":
            g[j] = 1
        else:
            g[j] = 1 - g[j - 1]
    for _ in range(q):
        x, y = map(int, input().split())
        res = f[x] ^ g[y] ^ f[1]
        if res == 1:
            print("Yes")
        else:
            print("No")
