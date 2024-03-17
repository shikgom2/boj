import sys
input = sys.stdin.readline

K, N = map(int, input().split())

li = [int(input()) for _ in range(K)]

left = 1
right = max(li)
mid = (left + right) // 2

while left <= right:
    mid = (left + right) // 2
    
    count = 0
    for n in li:
        count += n // mid
        
    if count >= N:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)