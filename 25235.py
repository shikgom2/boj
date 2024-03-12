N = int(input())
li = map(str, input().split())
d = {}
for i in li:
    d[i] = 0

for i in range(N):
    j = map(str, input().split())
    for k in j:
        d[k] += 1
d = sorted(d.items(), key=lambda item: item[1], reverse=True)
for i in d:
    print(f'{i[0]} {i[1]}')