a = list(map(str, input()))
small = [1,0,0,2]
for i in a:
    if i == 'A':
        small[0], small[1] = small[1],small[0]
    elif i == 'B':
        small[0], small[2] = small[2],small[0]
    elif i == 'C':
        small[0], small[3] = small[3],small[0]
    elif i == 'D':
        small[1], small[2] = small[2],small[1]
    elif i == 'E':
        small[1], small[3] = small[3],small[1]
    elif i == 'F':
        small[2], small[3] = small[3],small[2]

print(small.index(1)+1)
print(small.index(2)+1)