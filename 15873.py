s = input()

if len(s) >= 3 and s[1] == '0':
    A = int(s[:2])
    B = int(s[2:])
else:
    A = int(s[0])
    B = int(s[1:])

result = A + B
print(result)