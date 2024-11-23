import sys
input = sys.stdin.readline 

f1 = 0
f2=  0
for _ in range(9):
    s = input().rstrip()
    if(s == 'Tiger'):
        f1 += 1
    else:
        f2 += 1

if(f1>f2):
    print("Tiger")
else:
    print("Lion")