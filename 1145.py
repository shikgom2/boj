import sys
input = sys.stdin.readline

li = list(map(int, input().split()))

for i in range(1, 10**10):
    cnt = 0
    for j in range(5):
        if(i % li[j] == 0):
            cnt += 1
    if(cnt >= 3):
        print(i)
        break