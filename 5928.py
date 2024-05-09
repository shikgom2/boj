d,h,m = map(int, input().split())
st = 11*60+11
et = ((d-11)*24*60)+h*60+m
t=et-st
if t >= 0:
    print(t)
else:
    print(-1)