def compute_lps_array(pattern):
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

pattern = input()
#lps = compute_lps_array(pattern)
ans = 0
for i in range(len(pattern)):
    ans = max(ans, max(compute_lps_array(pattern[i:])))

print(ans, end="")