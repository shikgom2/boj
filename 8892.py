import sys
input = sys.stdin.readline

def is_palindrome(s):
    return s == s[::-1]

t = int(input())
for _ in range(t):
    n = int(input())
    li = []
    for __ in range(n):
        s = input().rstrip()
        li.append(s)
    
    flag = False
    ans = ''
    for i in range(n):
        for j in range(n):
            if(i==j):
                continue
            else:
                s = li[i] + li[j]
                if(is_palindrome(s)):
                    flag = True
                    ans = s
                    break
    if(flag):
        print(ans)
    else:
        print(0)