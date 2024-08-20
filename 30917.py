import sys
input = sys.stdin.readline

ask = False
a = 1
b = 1
while True:
    if(ask == False):
        print("? A", a, flush=True) #ask
        a += 1
    else:
        print("? B", b, flush=True)
        b += 1
    resp = int(input())

    if(resp == 1 and ask == True):
        print("!", a + b - 2)
        break

    if(resp == 1 and ask == False):
        ask = True