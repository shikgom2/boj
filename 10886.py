import sys
input = sys.stdin.readline

i = int(input())

a,b = 0,0

while(True):
    i = i-1

    j = int(input())

    if(j == 0):
        a = a+1
    elif(j == 1):
        b = b+1

    if(i == 0):
        break

if(a>b):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")