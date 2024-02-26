import math
n = 1001

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
arr = list(map(int, input().split()))
cnt = 0
for a in arr:
    if(array[a]):
        cnt += 1
print(cnt)