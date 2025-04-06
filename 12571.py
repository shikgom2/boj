import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    n = int(input())
    li = []
    for _ in range(n):
        a, b = map(int, input().split())
        li.append((a, b))
    
    li.sort(key=lambda x: x[0])
    
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if li[i][1] > li[j][1]:
                ans += 1
    
    print("Case #{}: {}".format(t, ans))
