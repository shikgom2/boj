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

n, k = map(int, input().split())
s = list(map(str, input().strip()))

s.reverse()
ans = z(s)
print(ans)
if(ans[0] == k):
    print(ans[0])
else:
    ans = ans[1:]
    m2 = max(ans)
    m = 0
    for i in ans:
        if(i == 0):
            m = 0
        else:
            m = max(m, i)
    if(m != 0):
        m = m + k
    print(max(m, m2))