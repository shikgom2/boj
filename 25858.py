n, d = map(int, input().split())
li = []

for _ in range(n):
    li.append(int(input()))

for i in li:
    print(d * i // sum(li))