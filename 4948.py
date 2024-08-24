import sys
input = sys.stdin.readline 
import math

array = [True for i in range(300001)]

for i in range(2, int(math.sqrt(300000)) + 1):
    if array[i] == True:
        j = 2 
        while i * j <= 300000:
            array[i * j] = False
            j += 1
            
while(True):
    n=int(input())
    if(n==0):
        break
    ans = 0
    for i in range(n+1, n*2+1):
        if(array[i]):
            ans +=1
    print(ans)