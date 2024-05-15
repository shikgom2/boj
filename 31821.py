n = int(input())
li = []

for _ in range(n):
    i = int(input())
    li.append(i)

k = int(input())
ans = 0
for _ in range(k):
    a = int(input())
    ans += li[a-1]

print(ans)