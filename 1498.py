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

s = input()
f = failure(s)
for i in range(1, len(s)):
    l = (i+1) - f[i]
    if(f[i] and (i+1) % l == 0):
        print(f'{i+1} {(i+1)//l}')
