n = int(input())
res = 0

li = []
for _ in range(n):
    tmp = int(input())
    li.append(tmp)

li.sort()

max = -1
for i in range(len(li)):
    if(max < li[i] * (n-i)):
        max = li[i] * (n-i)
print(max)