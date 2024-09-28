import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    ans = 0

    for i in range(1, n):
        for j in range(i):
            if(li[i] >= li[j]):
                ans +=1

    print(ans)        