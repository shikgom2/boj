import sys
input = sys.stdin.readline

n,l =  map(int, input().split())

for i in range(l, 101):
    tg = n - i * (i + 1) // 2
    if tg % i == 0:
        x = tg // i + 1
        if x >= 0:
            for length in range(i):
                print(length + x, end=" ")
            exit()
print(-1)