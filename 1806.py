N, S = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0
sum = 0
mins = N + 1 

while right < N:
    if sum < S:
        sum += nums[right]
        right += 1
        
    while sum >= S:
        mins = min(mins, right - left)
        sum -= nums[left]
        left += 1

if mins == N + 1:
    print("0")
else:
    print(mins)