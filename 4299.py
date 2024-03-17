i,j=map(int,input().split())
x = int((i + j)/2)
y = int((i - j)/2)
if x + y != i or x > y and x - y != j or x < y and y - x != j or x < 0 or y < 0:
    print('-1')
else:
    print(x, y)