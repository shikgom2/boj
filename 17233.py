import math
import sys
input = sys.stdin.readline

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

lists = []

N = int(input())
for _ in range(N):
    tmp = list(map(str, input().split()))
    lists.append(tmp[1])

target = list(map(str, input().split()))
target = target[1]

counts = []
indices = []
for i in range(len(lists)):
    lps = failure(lists[i])
    count, indice = kmp(target, lists[i], lps)
    counts.append(count)
    indices.append(indice)

print(count)
print(indices)