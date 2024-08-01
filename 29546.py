n = int(input())
li = [0]
for _ in range(n):
    li.append(input())

m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        print(li[i])