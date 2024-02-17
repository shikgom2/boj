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
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return True
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

n = int(input())
list1 = list(map(int, input().split())) 
list2 = list(map(int, input().split())) 
list1 = sorted(list1)
list2 = sorted(list2)

check1 = [0] * 720001
check2 = [0] * 360001

for lists in list1:
    check1[lists] = 1
    check1[lists + 360000] = 1
for lists in list2:
    check2[lists] = 1

lps = failure(check2)
fun1 = kmp(check1, check2, lps)

if(fun1):
    print("possible")
else:
    print("impossible")