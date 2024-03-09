a = list(map(str, input()))
s = [1,0,0,2]
for i in a:
    if (i == 'A'):
        s[0], s[1] = s[1], s[0]
    elif (i == 'B'):
        s[0], s[2] = s[2], s[0]
    elif (i == 'C'):
        s[0], s[3] = s[3], s[0]
    elif (i == 'D'):
        s[1], s[2] = s[2], s[1]
    elif(i == 'E'):
        s[1], s[3] = s[3], s[1]
    elif (i == 'F'):
        s[2], s[3] = s[3], s[2]

print(s.index(1)+1)
print(s.index(2)+1)