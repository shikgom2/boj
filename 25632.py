import math
n=1001
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1

n = list(map(int, input().split()))
m = list(map(int, input().split()))

li = []
li2 = []
for i in range(n[0], n[1]+1):
    if(array[i] == True):
        li.append(i)
for i in range(m[0], m[1]+1):
    if(array[i] == True):
        li2.append(i)

n = set(li)
m = set(li2)

res = n.intersection(m)

len1 = len(n) - len(res)
len2 = len(m) - len(res)

if(len(res) % 2 == 1):
    len1 += 1

if(len1 <= len2):
    print("yj")
else:
    print("yt")