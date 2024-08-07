from functools import cmp_to_key

n = int(input())
li = list(input().split())
li.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True) #>0: x,y <0: y,x
print(*li)