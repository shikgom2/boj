import sys
input = sys.stdin.readline

def solve(arr):
    n = len(arr)
    if n == 0:
        return (0, 0), []
    
    prefix_sums = [(0, -1)]
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        prefix_sums.append((current_sum, i))
    
    prefix_sums.sort()
    
    min_diff = float('inf')
    closest_pair = (0, 0)
    
    for i in range(1, len(prefix_sums)):
        diff = abs(prefix_sums[i][0] - prefix_sums[i - 1][0])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (prefix_sums[i - 1][1], prefix_sums[i][1])
    
    start = min(closest_pair) + 1
    end = max(closest_pair)
    
    return (start, end), arr[start:end + 1]

n = int(input())
li = list(map(int, input().split()))
ans = solve(li)

print(sum(ans[1]))
print(ans[0][0]+1, ans[0][1]+1)
