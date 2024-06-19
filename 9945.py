t = 1
while(True):
    n = input()
    if(n == ''):
        t += 1
        continue
    if(int(n) < 0):
        break
    x,y,s=0,0,0
    for _ in range(int(n)):
        i, j, k=map(int,input().split())
        x += i * k
        y += j * k
        s += k
    print('Case %d: %.2f %.2f' %(t, round(x/s,2), round(y/s,2)))