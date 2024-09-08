import sys
input = sys.stdin.readline 

def check(li, mid):
    tmp = 0
    for i in range(n):
        for j in range(n):
            tmp += min(mid, li[i][j])
    return tmp

n = int(input())
li = []
ss = 0
for _ in range(n):
    a = list(map(int, input().split()))
    li.append(a)
    ss += sum(a)

low, high = 0, 10**20
ans = 0

while low <= high:
    mid = (low + high) // 2
    if (check(li, mid) * 2 >= ss):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)