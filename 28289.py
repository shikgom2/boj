n = int(input())
a,b,c,d = 0,0,0,0
for _ in range(n):
    i,j,k = map(int, input().split())
    if(i == 1):
        d+=1
    elif(j==1 or j==2):
        a+=1
    elif(j==3):
        b+=1
    elif(j==4):
        c+=1
print(a)
print(b)
print(c)
print(d)