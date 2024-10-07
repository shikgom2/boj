import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    li = []
    for _ in range(m):
        k,d,a= map(int, input().split())
        li.append((k,d,a))
    
    a,b,c = map(int, input().split())
    ans = 0
    for i in range(m):
        tmp = li[i][0] * a + li[i][2]*c - li[i][1]*b
        tmp = max(0, tmp)
        ans += tmp
    print(ans)