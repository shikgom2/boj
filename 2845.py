n,m = map(int, input().split())
n = n*m
li = list(map(int, input().split()))
for i in range(len(li)):
    li[i] = li[i] - n
print(*li)