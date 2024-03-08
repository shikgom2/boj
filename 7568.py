N = int(input())
li = []
for _ in range(N):
    x, y = map(int, input().split())
    li.append((x, y))

for a in li:
    m = 0
    for b in li:
        if a[0] < b[0] and a[1] < b[1]:
            m += 1
    print(m + 1, end=" ")