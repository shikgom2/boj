import sys
input = sys.stdin.readline

def solve(num):
    ans = 0
    for i in range(num):
        if(li[i] > li2[m-num+i]):
            ans += li[i] - li2[m-num+i]

    return ans <= x

n,m,x = map(int, input().split()) 

li = list(map(int, input().split()))
li2 = list(map(int, input().split()))

li.sort()
li2.sort()

s = 0
e = min(n,m)

while(e - s > 10):
    mid = (s + e) // 2
    if(solve(mid)):
        s = mid
    else:
        e = mid-1

for i in range(e, s-1, -1):
    if(solve(i)):
        print(i)
        exit()
print(-1)