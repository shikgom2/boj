def is_palindrome(s):
    return s == s[::-1]

while(True):
    i = input()
    if(i=="0"):
        break
    if(is_palindrome(i)):
        print("yes")
    else:
        print("no")