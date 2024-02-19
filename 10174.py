def is_palindrome(s):
    return s == s[::-1]

N = int(input())
while(True):
    N -= 1
    i = input()
    i = i.lower()
    if(is_palindrome(i)):
        print("Yes")
    else:
        print("No")
    if(N == 0):
        break