x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))

c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
if(c>0):
    print(1)
elif(c<0):
    print(-1)
else:
    print(0)