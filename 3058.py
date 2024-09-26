import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    li = list(map(int, input().split()))
    tmp = []
    for i in range(len(li)):
        if(li[i] % 2 == 0):
            tmp.append(li[i])
    
    print(sum(tmp), min(tmp))
