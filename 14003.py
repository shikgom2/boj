from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

li = [a[0]]
memo = [0 for _ in range(n)]

for idx, num in enumerate(a[1:], start = 1) :
    if li[-1] < num :
        li.append(num)
        memo[idx] = len(li)-1
    else :
        b_idx = bisect_left(li, num)
        li[b_idx] = num
        memo[idx] = b_idx
    
maxVal = len(li)
print(maxVal)