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
cnt = 1

def kmp(text, pattern, lps):

    i = 0
    j = 0
    count = 0
    indices = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == len(pattern):
                count += 1
                indices.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count

while(True):
    k = int(input())
    if(k == 0):
        break
    s = input()

    Z = failure(s)
    print(f"Test case #{cnt}")

    print(Z)
    for i in Z:
        if(i != 0):
            print(s[0:(i+1)])
            count = kmp(s, s[0:i], Z)
            #print(f"{i} {count}")
    cnt += 1 