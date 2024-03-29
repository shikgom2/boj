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

def optimized_string_removal(s, bomb):
    stack = []
    lps = failure(bomb)

    for char in s:
        stack.append(char)
        if len(stack) >= len(bomb) and char == bomb[-1]:
            if ''.join(stack[-len(bomb):]) == bomb:
                del stack[-len(bomb):]

    return ''.join(stack)

str_input = input()
bomb = input()

stack = []
lps = failure(bomb)

for char in str_input:
    stack.append(char)
    if len(stack) >= len(bomb) and char == bomb[-1]:
        if ''.join(stack[-len(bomb):]) == bomb:
            del stack[-len(bomb):]
print(''.join(stack))