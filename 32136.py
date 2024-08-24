import sys
input = sys.stdin.readline

def check(i, a):
    max_dist = 0
    for j in range(len(a)):
        max_dist = max(max_dist, abs(i - j) * a[j])
    return max_dist

def ternary_search(a, left, right):
    while right - left > 3:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if check(mid1, a) < check(mid2, a):
            right = mid2
        else:
            left = mid1

    min_value = float('inf')
    for i in range(left, right + 1):
        min_value = min(min_value, check(i, a))
    
    return min_value

n = int(input())
li = list(map(int, input().split()))

ans = ternary_search(li , 0, n - 1)
print(ans)

