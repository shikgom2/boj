import math
n = int(input())

left = 1
right = 10 ** 6

while(left <= right):
    mid = (left + right) // 2
    ans = math.factorial(mid)
    #print(mid)
    if(ans == n):
        print(mid)
        exit()
    elif(ans < n):
        left = mid + 1
    else:
        right = mid - 1