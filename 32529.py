import sys
input = sys.stdin.readline

n,m = map(int, input().split())
li = list(map(int, input().split()))

if(sum(li) < m):
    print(-1)
else:
    li.reverse()
    t = 0
    for i in range(n):
        t += li[i]
        if(t >= m):
            print(n - i)
            exit()