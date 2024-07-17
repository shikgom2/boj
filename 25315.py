import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if(c>0):
        return 1
    elif(c<0):
        return -1
    else:
        return 0
    
def is_test(x1, y1, x2, y2, x3, y3, x4, y4):
    f = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    f1 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    if f == -1 and f1 == -1:
        return True
    else:
        return False

n = int(input())
li = []
ans = 0
for _ in range(n):
    l = list(map(int, input().split()))
    li.append(l)

li.sort(key=lambda x : x[4])
for i in range(n):
    cnt = 1
    for j in range(i + 1, n):
        if(is_test(li[i][0], li[i][1], li[i][2], li[i][3], li[j][0], li[j][1], li[j][2], li[j][3])):
            cnt += 1

    ans += li[i][4] * cnt        
print(ans)