s=list(map(str, input().strip()))
s1=list(map(str, input().strip()))

while(1):

    if(len(s) == len(s1)):
        if(s == s1):
            print(1)
            break
        else:
            print(0)
            break
    if(s1[len(s1)-1] == 'A'):
        s1.pop()
    else:
        s1.pop()
        s1.reverse()