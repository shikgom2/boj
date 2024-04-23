k,n = map(int, input().split())

li = []
m=0
for _ in range(k):
    i = input()
    li.append(i)
    m = max(m, int(i))
for _ in range(n-k):
    li.append(str(m))

li.sort(key=lambda x: x*10, reverse=True)
print("".join(li))