a = int(input())
b = int(input())
ans = (a+b) % 12
if(ans == 0):
    ans = 12
print(ans)