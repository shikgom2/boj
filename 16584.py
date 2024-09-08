import sys
input = sys.stdin.readline

def check(li, mid): 
    sum = 0

    for i in range(n):
        if(li[i] < mid):
            sum += mid - li[i]
    return sum

n,k = map(int, input().split())
li = []
for _ in range(n):
    a = int(input())
    li.append(a)

s, e = 0, 10**10
ans = 1

while s <= e:
    m = (s + e) // 2
    if (check(li, m) <= k):
        ans = m
        s = m + 1
    else:
        e = m - 1

print(ans)