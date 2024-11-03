import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    li = []
    li2 = []
    for i in range(n):
        x, y = map(int, input().split())
        li.append((x, y, i+1))
        li2.append((x,y))
        
    dir = [(-1,0), (0,1), (1,0), (0,-1)]
    
    ans = []
    ans2 = []
    
    li.sort(key=lambda x:(x[0], x[1]))
    
    for i in range(n):
        for j in range(4):
            dx = li[i][0] + dir[j][0]
            dy = li[i][1] + dir[j][1]

            if(dx > 10**9 or dy > 10**9 or dx < -10**9 or dy < -10**9):
                continue
            
            if (dx, dy) not in li2 and (dx, dy) not in ans:
                ans.append((dx,dy))
                ans2.append((li[i][2], dx, dy))
                break
    
    for i in range(len(ans2)):
        print(ans2[i][0], ans2[i][1], ans2[i][2])