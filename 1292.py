li = []
for i in range(1, 50):
    for j in range(0, i):
        li.append(i)

i,j = map(int, input().split())

res = 0
for a in range(i-1, j):
    res += li[a]
print(res)