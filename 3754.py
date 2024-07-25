import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    res = 0
    flag = 0

    for i in li:
        res ^= i
        flag = flag | (res > 1)

    if(flag):
        if(res):
            print("John")
        else:
            print("Brother")
    else:
        if(res):
            print("Brother")
        else:
            print("John")