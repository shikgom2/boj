import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    li = []
    n = int(input())

    for _ in range(n):
        a,b = map(int, input().split())
        li.append((a,b))

    li.sort()

    ans = 1
    min_b = li[0][1]
    for i in range(1,n):
        if (min_b > li[i][1]) :
            ans += 1
            min_b = li[i][1]

    print(ans)