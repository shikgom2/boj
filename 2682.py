import sys
input = sys.stdin.readline
from math import factorial

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    if(k == 1):
        print(factorial(n - 1))
    else:
        ans = 0
        for j in range(2, k + 1):
            cur = (factorial(k - 2) // (factorial(j - 2) * factorial(k - j))) * factorial(j - 1) * factorial(n - j)
            ans += cur

        print(ans)