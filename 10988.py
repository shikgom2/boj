def is_palindrome(s):
    return s == s[::-1]

N = int(input())

i = input()
if(is_palindrome(i)):
    print("1")
else:
    print("0")
    