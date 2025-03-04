
N, E = map(int, input().split())
li = list(map(int, input().split()))

li.sort()

material_count = 1

prev = li[0]

for i in range(1, N):
    if li[i] - prev >= E:
        material_count += 1
    prev = li[i]

print(material_count)
