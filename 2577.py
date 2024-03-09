a = int(input())
b = int(input())
c = int(input())
r = str(a * b * c)
res = [0]*10

for i in r:
    for j in range(0,10):
        if i == f'{j}':
           res[j] += 1
for i in res:
    print(i)