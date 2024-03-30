n = int(input())
li =[]
for i in range(n):
    li.append(list(map(int,input().split())))
li.sort()
li=sorted(li,key=lambda x: x[-1])
#print(li)
n = 0
ans = 0
for i in li:
    if i[0] >= ans:
        n += 1
        ans = i[1]
print(n)