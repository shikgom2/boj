from functools import cmp_to_key

li = []
while True:
    try:
        n = input()
        li.append(n)
    except Exception:
        break

li.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True) #>0: x,y <0: y,x

ans = ''.join(li).lstrip('0')
if(ans == ""):
    print(0)    
else:
    print(ans)
