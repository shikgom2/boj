import re

p = re.compile(r'^(?:100+1+|01)+$')
t = int(input())
for _ in range(t):
    s = input().strip()
    if p.match(s): 
        print("YES")
    else:
        print("NO")