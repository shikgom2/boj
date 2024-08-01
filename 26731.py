import string

s = input()
for i in list(string.ascii_uppercase):
    if i not in s:
        print(i)