def solve():
    i,j = map(int, input().split())
    ans = 1
    for _ in range(j):
        ans = ans * i % 10
    ans = ans % 10
    if(ans == 0):
        print(10)
    else:
        print(ans)

t = int(input())
for _ in range(t):
    solve()