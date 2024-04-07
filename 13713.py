def z(s):
    n = len(s)
    l, r = -1, -1
    Z = [0] * n
    Z[0] = n
    
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > r:
            l, r = i, i + Z[i] - 1
    return Z

s = list(map(str, input().strip()))
c = int(input())
s.reverse()

ans = z(s)
for _ in range(c):
    i = int(input())
    print(ans[len(s) - i])