import sys
input = sys.stdin.readline

li = []

n = int(input())
li = list(map(str, input().rstrip()))

h = 0
m = 0
if(n == 1):
    print("HM")
    exit()
    
for i in range(len(li)):
    if(li[i] == 'H'):
        h += 1
    else:
        m += 1

add = 0
if(li[n-2] == 'H' and li[n-1] == 'H'):
    add = -2
elif(li[n-2] == 'M' and li[n-1] == 'H'):
    add = -1
elif(li[n-2] == 'M' and li[n-1] == 'M'):
    add = 2

if(add > 0):
    if((h-m) + add > 0):
        print('H')
    else:
        print("M")
else:
    if((h-m) + add >= 0):
        print("H")
    else:
        print("M")