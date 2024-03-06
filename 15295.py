t = int(input())
res = []

for i in range(t):
    k,n = map(int, input().split())
    h = 0
    for i in range(1,n+1):
        h += i
    h += n
    res.append(f'{k} {h}')

for i in res:
    print(i)    