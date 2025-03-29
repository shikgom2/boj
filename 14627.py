import sys
input =  sys.stdin.readline

s, c = map(int, input().split())
li = [int(input()) for _ in range(s)]

leng = sum(li)

lo, hi = 1, max(li)
best = 0

while lo <= hi:
    mid = (lo + hi) // 2
    count = 0
    
    for L in li:
        count += L // mid
        if count >= c:
            break
    
    if count >= c:
        best = mid
        lo = mid + 1
    else:
        hi = mid - 1
        
l = c * best

print(leng - l)
