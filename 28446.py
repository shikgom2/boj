import sys
input = sys.stdin.readline

dir = dict()

n = int(input())
for _ in range(n):
    li = list(map(int, input().split()))
    if(li[0] == 1):
        x = li[1]
        y = li[2]
        
        if y not in dir:
            dir[y] = x
        else:
            dir[y] = x
    else:
        y = li[1]
        print(dir[y])    
        