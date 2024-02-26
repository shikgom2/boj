k, n = map(int, input().split())
res = 0

li = []
for _ in range(k):
    tmp = int(input())
    li.append(tmp)

li.sort(reverse=True)

for i in range(len(li)):
    res += n // li[i]
    n %= li[i]
print(res)