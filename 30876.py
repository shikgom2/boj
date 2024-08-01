n = int(input())
li = []
for _ in range(n):
    x, y = map(int, input().split())
    li.append([y, x])

print(*(min(li)[::-1]))