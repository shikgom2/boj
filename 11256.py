import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    j, n = map(int, input().split())

    li = []
    for _ in range(n):
        a, b= map(int, input().split())
        li.append(a*b)

    li.sort(reverse=True)

    ans = 0
    for i in range(len(li)):
        ans += 1
        j -= li[i] 
        if(j <=0):
            break
    print(ans)