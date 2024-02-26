def manacher(s):
    A = '@#' + '#'.join(s) + '#$'
    Z = [0] * len(A)
    center = right = 0

    for i in range(1, len(A) - 1):
        if i < right:
            Z[i] = min(right - i, Z[2 * center - i])
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
        if i + Z[i] > right:
            center, right = i, i + Z[i]

    maxLen, centerIndex = max((n, i) for i, n in enumerate(Z))
    start = (centerIndex - maxLen) // 2
    return s[start:start + maxLen]

s = input()
print(len(manacher(s)))