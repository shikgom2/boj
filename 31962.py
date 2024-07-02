import sys
input = sys.stdin.readline

li = []

n,x = map(int, input().split())

cnt = 0
mint = 0

ans = 0

for _ in range(n):
    s, t = map(int, input().split())

    if(s+t <= x):
        cnt += 1
        
        if(s >= mint):
            ans = s
            mint = s

if(cnt):
    print(ans)
else:
    print(-1)