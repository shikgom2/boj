import sys
input = sys.stdin.readline

def mamacher(li):
    l = 2 * len(li) + 2
    nums = [-1] * l
    for i in range(1, len(li) + 1):
        nums[2 * i] = li[i - 1]
        
    A = [0] * l
    b, c = 0, 0

    for i in range(1, l):
        if i > b:
            A[i] = 0
        else:
            A[i] = min(A[2 * c - i], b - i)
        
        while i - A[i] - 1 > 0 and i + A[i] + 1 < l and nums[i - A[i] - 1] == nums[i + A[i] + 1]:
            A[i] += 1
        
        if i + A[i] > b:
            b = i + A[i]
            c = i
    return A

l = int(input())
li = list(map(int, input().split()))
ans = mamacher(li)

t = int(input())

for _ in range(t):
    s, e = map(int, input().split())
    if ans[s + e] > e - s:
        print(1)
    else:
        print(0)