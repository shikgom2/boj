def failure(pattern):
    lps = [0] * len(pattern)
    length = 0
    
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

s, k = map(str, input().split())
k = int(k)
Z = failure(s)
print((len(s) * k) - (Z[len(s) - 1] * (k-1)))