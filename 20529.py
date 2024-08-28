import sys
input = sys.stdin.readline
import itertools
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().rstrip()
    li = s.split(" ")

    if(n >= 33):
        print(0)
        continue

    permu = itertools.combinations(li, 3)
    permu = list(permu)
    
    ans = 10**10
    for i in range(len(permu)):
        tmp = 0
        for j in range(4):        
            if(permu[i][0][j] != permu[i][1][j]):
                tmp += 1
            if(permu[i][1][j] != permu[i][2][j]):
                tmp += 1
            if(permu[i][0][j] != permu[i][2][j]):
                tmp += 1
        ans = min(ans, tmp)
        
    print(ans)