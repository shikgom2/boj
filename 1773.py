N, C = map(int, input().split())

li = []
for _ in range(N):
    i = int(input())
    li.append(i)
li.sort()
res = 0
for i in range(1, C + 1):
    for j in li:
        if i % j == 0:
            res += 1
            break
print(res)