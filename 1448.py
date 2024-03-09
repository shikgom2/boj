N = int(input())
li = []

for _ in range(N):
    i = int(input())
    li.append(i)

li.sort(reverse=True)
for i in range(0, len(li)-2):
    if(li[i] < li[i+1] + li[i+2]):
        print(li[i] + li[i+1] + li[i+2])
        exit()
print(-1)