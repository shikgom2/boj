import sys
input = sys.stdin.readline
from itertools import permutations

def expr(array):
  result = 0
  for i in range(n - 1):
    result += abs(array[i] - array[i + 1])
  return result
  
n = int(input())
li = list(map(int, input().split()))

ans = 0
for i in permutations(li):
    res = 0
    for j in range(n - 1):
        res += abs(i[j] - i[j + 1])  

    ans = max(ans, res)

print(ans)