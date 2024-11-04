import sys
input = sys.stdin.readline

t = int(input())
cura=  0
curb = 0
flag = True
for _ in range(t):
    a,b = map(int, input().split())
    if(cura <= a and curb <= b):
        cura = a
        curb = b
    else:
        flag = False
        break
if(flag):
    print("yes")
else:
    print("no")