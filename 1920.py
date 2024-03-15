import sys
input = sys.stdin.readline

def bs(li, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if li[mid] == target:
            return 1
        elif li[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

n = int(input())
li = list(map(int, input().split()))
li.sort()

n = int(input())
li2 = list(map(int, input().split()))

for n in li2:
    print(bs(li, 0, len(li) - 1, n))
