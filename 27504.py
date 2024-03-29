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
    return count

N = int(input())
temp = [list(map(int, input().split())) for _ in range(N)]

songs = []
for i in range(N):
    tmp = []
    for j in range(1, len(temp[i]) - 1):    
        tmp.append(temp[i][j+1] - temp[i][j])
    songs.append(tmp)

L = int(input())
temp = list(map(int, input().split()))
melody = []

for i in range(L-1):
    melody.append(temp[i+1] - temp[i])

lps = failure(melody)

flag = False
for i in range(0, N):
    count = kmp(songs[i], melody, lps)
    if(count > 0):  
        print(i+1, end=" ")
        flag = True
if(flag == False):
    print(-1)