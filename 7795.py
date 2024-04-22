import sys
input = sys.stdin.readline

def solve():
    i,j = map(int, input().split())
    li = list(map(int ,input().split()))
    li2 = list(map(int, input().split()))

    li.sort()
    li2.sort()
    ans = 0
    idx=0
    for i in range(len(li)):
        while idx < j:
            if li[i] > li2[idx]:
                idx += 1
            else:
                break    
        ans += idx
    print(ans)

t = int(input())
for _ in range(t):
    solve()