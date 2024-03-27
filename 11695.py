m, n = map(int, input().split())

res = 0
li = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    li.append(sum(tmp))

for i in li:
    res = res ^ i

if(res == 0):
    print("ainta")
else:
    print("august14")
