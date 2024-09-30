import sys
input = sys.stdin.readline

def check(x):
    min_t = 0
    max_t = n - 1
    for i in range(n):
        t = x // li[i] #t / aj
        min_t = max(min_t, i - t) #left end
        max_t = min(max_t, i + t) #right end

    if(min_t <= max_t):
        return True #can
    else:
        return False #cant

n = int(input())
li = list(map(int, input().split()))

left = 0
right = max(li) * n
ans = -1

while left <= right:
    mid = (left + right) // 2

    if (check(mid)): #can all melt in T
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)

