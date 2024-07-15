import sys
input = sys.stdin.readline
import math

n = 7368787
array = [True for i in range(n + 1)]
array[0] = False
array[1] = False
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1


k = int(input())
cur = 0
for i in range(n):
    if(array[i]):
        cur += 1

    if(cur == k):
        print(i)
        exit()