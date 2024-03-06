k = int(input())
a = input()
u,o,s,p,c=0,0,0,0,0

for i in a:
    if(i == "u"):
        u+=1
    elif(i=="o"):
        o+=1
    elif(i=="s"):
        s+=1
    elif(i=="p"):
        p+=1
    elif(i=="c"):
        c+=1
print(min(u,o,s,p,c))