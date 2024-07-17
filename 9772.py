def check(s):
    idx = 0
    slen = len(s)
    if s[0] == '+' or s[0] == '-':
        idx += 1
    while idx < slen and s[idx] == '0':
        idx += 1
    if idx < slen and s[idx] == '.':
        idx += 1
        while idx < slen and s[idx] == '0':
            idx += 1

    return idx == slen


while True:
    x, y = input().split()
    if(x == 0 and y == 0):
        exit()
        
    if check(x) and check(y):
        break
    if check(x) or check(y):
        print("AXIS")
    else:
        if x[0] == '-':
            if y[0] == '-':
                print("Q3")
            else:
                print("Q2")
        else:
            if y[0] == '-':
                print("Q4")
            else:
                print("Q1")

print("AXIS")
