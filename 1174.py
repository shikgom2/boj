import sys
input = sys.stdin.readline
from collections import deque

def solve(n):
    li = []
    q = deque(range(10))
    
    while q:
        num = q.popleft()
        li.append(num)

        last_digit = num % 10
        for digit in range(last_digit):
            q.append(num * 10 + digit)

    if n <= len(li):
        return li[n - 1]
    else:
        return -1

n = int(input())
print(solve(n))
