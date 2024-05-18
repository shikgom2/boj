import sys
input = sys.stdin.readline

n, c = map(int, (input().split()))
li = [int(input()) for _ in range(n)]

def solved(d):
    count = 1   
    cur_house = li[0]
    for i in range(1, n):
        if cur_house + d <= li[i]: 
            count += 1
            cur_house = li[i]
    return count

li = sorted(li)
start, end = 1, li[-1] - li[0]

while start <= end:
    mid = (start+end) // 2
    
    if solved(mid) >= c:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(ans)