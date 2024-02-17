result = []
def manacher(s):
    A = '@#' + '#'.join(s) + '#$'
    Z = [0] * len(A)
    center = right = 0

    for i in range(1, len(A) - 1):
        if i < right:
            Z[i] = min(right - i, Z[2 * center - i])
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
            start = (i - Z[i]) // 2
            end = start + Z[i]
            if Z[i] > 0:
                result.append(s[start:end])
        if i + Z[i] > right:
            center, right = i, i + Z[i]

    maxLen, centerIndex = max((n, i) for i, n in enumerate(Z))
    start = (centerIndex - maxLen) // 2
    return s[start:start + maxLen]

s = input()
manacher(s)

cnt = 0
for res in result:
    if(len(res) > 1 and len(res) % 2 == 1):
        print(res)
        cnt += 1

print(cnt + len(s))