from functools import cmp_to_key #조건 정렬 모듈 import

n = int(input())
arr = input().split() #문자열로 입력받자.

arr.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True) #>0: x,y <0: y,x

ans = ''.join(arr).lstrip('0') #예외처리
if(ans == ""):
    print(0)
else:
    print(ans)


