import sys
input = sys.stdin.readline

def move(map, nr, nc, dir): 
    ans = 0
    while(True):
        if(ans == 1000000):
            return ans
        
        if(dir == 'R'):
            nc += 1
        elif(dir == 'L'):
            nc -=1
        elif(dir == 'U'):
            nr -=1 
        elif(dir == 'D'):
            nr += 1

        #print(nr, nc, dir)
        
        ans += 1
        if(nc == -1 or nc == m or nr == -1 or nr == n):
            return ans
        
        if(map[nr][nc] == 'C'):
            return ans
        
        if(map[nr][nc] == '\\'):
            if(dir == 'R'):
                dir = 'D'
            elif(dir == 'D'):
                dir = 'R'
            elif(dir == 'U'):
                dir = 'L'
            elif(dir == 'L'):
                dir = 'U'

        if(map[nr][nc] == '/'):
            if(dir == 'R'):
                dir = 'U'
            elif(dir == 'D'):
                dir = 'L'
            elif(dir == 'U'):
                dir = 'R'
            elif(dir == 'L'):
                dir = 'D'

n,m = map(int, input().split())
maps= []
for _ in range(n):
    li = list(map(str, input().rstrip()))
    maps.append(li)
    
nx, ny = map(int, input().split())
nx-=1
ny-=1

ans1 = move(maps, nx, ny, 'U')
ans2 = move(maps, nx, ny, 'R')
ans3 = move(maps, nx, ny, 'D')
ans4 = move(maps, nx, ny, 'L')
#print(ans1, ans2, ans3, ans4)

if(ans1 == 1000000):
    print("U")
    print("Voyager")
elif(ans1 >= ans2 and ans1 >= ans3 and ans1 >= ans4):
    print("U")
    print(ans1)
elif(ans2 == 1000000):
    print("R")
    print("Voyager")
elif(ans2 >= ans1 and ans2 >= ans3 and ans2 >= ans4):
    print("R")
    print(ans2)
elif(ans3 == 1000000):
    print("D")
    print("Voyager")
elif(ans3 >= ans2 and ans3 >= ans1 and ans3 >= ans4):
    print("D")
    print(ans3)

elif(ans4 == 1000000):
    print("L")
    print("Voyager")
elif(ans4 >= ans2 and ans4 >= ans3 and ans4 >= ans1):
    print("L")
    print(ans4)