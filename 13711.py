def lcs_length(X, Y):
    m, n = len(X), len(Y)
    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        current = [0] * (n + 1)
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                current[j] = prev[j - 1] + 1
            else:
                current[j] = max(prev[j], current[j - 1])
        prev = current
    return prev

def hirschberg(X, Y):
    m, n = len(X), len(Y)
    if m == 0:
        return ""
    elif n == 0:
        return ""
    elif m == 1:
        if X[0] in Y:
            return X[0]
        else:
            return ""
    else:
        i = m // 2
        L1 = lcs_length(X[:i], Y)
        L2 = lcs_length(X[i:][::-1], Y[::-1])
        k = max(range(n + 1), key=lambda j: L1[j] + L2[n - j])
        return hirschberg(X[:i], Y[:k]) + hirschberg(X[i:], Y[k:])

n = int(input())
x = list(map(str, input().split()))
y = list(map(str, input().split()))
x = ''.join(x)
y = ''.join(y)

lcs = hirschberg(x,y)
print(len(lcs))
