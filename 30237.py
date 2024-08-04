import sys
input = sys.stdin.readline 

def solve():
    n = int(input())
    li = []
    for _ in range(n):
        l = list(map(int, input().split()))
        del l[0]
        li.append(l)
    
    u = set()
    for v in li:
        u.update(v)
    
    ans = 0
    for r in u:
        u2 = set()
        for v in li:
            if r not in v:
                u2.update(v)
        ans = max(ans, len(u2))

    if(n == 1):
        print(0)
        return
    else:
        print(ans)

    
t =int(input())
for _ in range(t):
    solve()