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

n = int(input())
list1 = list(map(str, input().split())) 
list2 = list(map(str, input().split())) 

list1 = list1 * 2
list1.pop()

lps = failure(list2)
count = kmp(list1, list2, lps)
length = len(list2)

if(count > length or count == length):
    print("1/1")
else:
    gcd = math.gcd(count, length)
    print(f'{count//gcd}/{length//gcd}')