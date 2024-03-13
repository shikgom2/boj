def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if(c>0):
        return 1
    elif(c<0):
        return -1
    else:
        return 0
    
x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
f = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
f1 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

if f == -1 and f1 == -1:
    print(1)
else:
    print(0)