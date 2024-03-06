a, b, c = map(int, input().split())
d = int(input())

h = d//3600
m = (d %3600)//60
s = (d%3600) % 60

a += h 
b += m 
c += s

if c >= 60:
    c -= 60 
    b += 1
if b >= 60:
    b -= 60
    a += 1
while a >= 24:
    a -= 24
print(a,b,c)