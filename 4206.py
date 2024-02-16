import sys

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

def kmp_search(text, pattern):
    lps = compute_lps_array(pattern)
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
    return count, indices

fibo = ["0"] * 101
fibo[0] = "0"
fibo[1] = "1"
for i in range(2, 21):
    fibo[i] = str(fibo[i-1]) + str(fibo[i-2])

text = int(input())
pattern = input()
    
count, indices = kmp_search(fibo[text+1], pattern)
cnt = 1
print(f"Case {cnt}: {count}")
cnt = cnt + 1
'''
for i in indices:
    print(int(i+1), end=' ')
'''