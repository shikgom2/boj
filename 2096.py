n = int(input())
a,b,c = (map(int, input().split()))

max1, max2, max3 = a, b, c
min1, min2, min3 = a, b, c

for i in range(1, n):
    a,b,c = (map(int, input().split()))

    temp1, temp2, temp3 = max1, max2, max3

    max1 = max(temp1 + a, temp2 + a)
    max2 = max(temp1 + b, temp2 + b, temp3 + b)
    max3 = max(temp2 + c, temp3 + c)

    temp1, temp2, temp3 = min1, min2, min3

    min1 = min(temp1 + a, temp2 + a)
    min2 = min(temp1 + b, temp2 + b, temp3 + b)
    min3 = min(temp2 + c, temp3 + c)    

print(f'{max(max1, max2, max3)} {min(min1, min2, min3)}')