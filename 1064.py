x1,y1,x2,y2,x3,y3 = map(int, input().split())

if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1):
    print(-1.0)
else: 
    t1 = ((x1 - x2)* (x1 - x2)+(y1-y2)* (y1-y2))**(1/2) + ((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))**(1/2)
    t2 = ((x1 - x2)* (x1 - x2) +(y1-y2)* (y1-y2))**(1/2) + ((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))**(1/2)
    t3 = ((x1 - x3) * (x1 - x3) +(y1-y3)*(y1-y3))**(1/2) + ((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))**(1/2)
    print(2 * (max(t1, t2, t3)-min(t1, t2, t3)))