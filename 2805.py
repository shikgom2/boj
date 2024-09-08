import sys
input = sys.stdin.readline

def check(li, m):
    tmp = 0
    for i in range(len(li)):
        if(li[i] > m):
            tmp += (li[i] - m)
    return tmp

n,k =map(int, input().split())
li = list(map(int, input().split()))

s, e = 0, 10**20
ans = 1

while s <= e:
    m = (s + e) // 2
    if (check(li, m) >= k):
        ans = m
        s = m + 1
    else:
        e = m - 1
print(ans)
