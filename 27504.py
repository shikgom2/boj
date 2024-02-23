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

N = int(input())
lists = [list(map(int, input().split())) for _ in range(N)]

L = int(input())
melody = list(map(int, input().split()))
min_melody = min(melody)

for i in range(N):
    min_ele = min(lists[i])
    for j in range(len(lists[i])):
        lists[i][j] -= min_ele



lps = failure(melody)

for i in range(N):
    count = kmp(lists[i], melody, lps)
    print(count)
#length = len(list2)
