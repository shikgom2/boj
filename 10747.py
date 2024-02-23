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

def kmp(text, pattern, lps):

    i = 0
    j = 0
    count = 0
    indices = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            #Find Pattern
            if j == len(pattern):
                count += 1
                indices.append(i - j)
                j = lps[j - 1]
        #Pattern different : find next index
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count, indices

str = input()
bomb = input()
stack = []

lps = failure(bomb)

for i in range(len(str)):
    stack.append(str[i])
    
    if(str[i] == bomb[len(bomb) - 1]):
        count, indicies = kmp(stack, bomb, lps)

        if(count > 0):
            for i in range(count):
                idx = indicies[i]
                del stack[idx:(idx + len(bomb))]
if stack:    
    print(''.join(stack))