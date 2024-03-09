import math
n = map(int, input().split())
m = map(int, input().split())
n = set(n)
m = set(m)

res = n.intersection(m)
    
len1 = len(n) - len(res)
len2 = len(m) - len(res)

if(len(res) % 2 == 1):
    len1 += 1

if(len1 <= len2):
    print("yj")
else:
    print("yt")