def failure(s):
    n = len(s)
    f = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = f[j-1]
        if s[i] == s[j]:
            j += 1
            f[i] = j
    return f

a = input()
b = input()
ans = []
f = failure(b)
dp = [0] * (len(a) + 1)
j = 0
for i in range(len(a)):
    ans.append(a[i])
    while j > 0 and a[i] != b[j]:
        j = f[j-1]
    if a[i] == b[j]:
        j += 1
    if j == len(b):
        del ans[-len(b):]
        j = dp[len(ans)]
    dp[len(ans)] = j
print(''.join(ans))