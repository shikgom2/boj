import sys
input = sys.stdin.readline 

def solve():
    n = int(input())
    li = list(map(int, input().split()))
    ans = []
    cur = 1

    for i in range(len(li)):
        if(li[i] == cur):
            cur += 2
        else:
            cur += 1
    print(cur-1)

t =int(input())
for _ in range(t):
    solve()