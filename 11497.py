import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    i = int(input())
    li = list(map(int, input().split()))
    
    li.sort()
    res = abs(li[0] - li[1])

    for j in range(2, len(li)):
        res = max(res, abs(li[j] - li[j-2]))

    print(res)