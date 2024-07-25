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


n, m = map(int, input().split())
li = list(map(int, input().split()))
pattern = list(map(int, input().split()))

li.reverse()
pattern.reverse()

flag = [False] * len(li)
lps = failure(pattern)
indices = kmp(li, pattern, lps)

kmp_result = indices[1]
check = [False] * n
ans = []

print(kmp_result)
for i in range(len(kmp_result)): 
    for j in range(kmp_result[i], kmp_result[i] + m):
        if(check[j] == False):
            check[j] = True

cur = 0
for i in range(len(check)):
    if(check[i]):
        cur += 1
    elif(cur > 0):
        ans.append(cur)
        cur = 0

if(cur > 0):
    ans.append(cur)

res = 0
for i in range(len(ans)):
    res = res ^ ans[i]

if(res):
    print("First")
else:
    print("Second")