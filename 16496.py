import sys
from functools import cmp_to_key
input = sys.stdin.readline

N = int(input())
arr = input().split()

arr.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)

answer = ''.join(arr).lstrip('0')
if(answer == ""):
    print(0)
else:
    print(answer)