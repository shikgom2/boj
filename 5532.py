l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

r1 = a//c
if(a%c != 0):
    r1 +=1
r2 = b//d
if(b%d != 0):
    r2 +=1
print(l - max(r1, r2))
