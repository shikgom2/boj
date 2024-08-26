import sys
input = sys.stdin.readline
import math

t = int(input())
for _ in range(t):
    n = int(input())

    dic = {}
    for i in range(n):
        a, b= map(str, input().rsplit())
        if(b not in dic):
            dic[b] = 1
        else:
            dic[b] += 1
    li = []
    for key, values in dic.items():
        li.append(values)
    
    ans = 1
    for i in range(len(li)):
        ans *= (li[i] + 1)
    ans -= 1
    print(ans)