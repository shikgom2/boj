li = []
for i in range(10):
    n = int(input())
    li.append(n % 42)
li = set(li)
print(len(li))