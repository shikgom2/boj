n = int(input())

two_d = [list(map(str, input().strip())) for _ in range(n)]

flag = True
for i in range(0, len(two_d[0])):
    txt = two_d[0][i]

    for j in range(1, n):
        if(txt != two_d[j][i]):
            flag = False

    if(flag):
        print(txt,end="")
    else:
        print("?",end="")
    flag= True
