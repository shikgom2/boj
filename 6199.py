N = int(input())
map = []
r = []
c = []

for i in range(N):
    line = input().strip()
    map.append(line)
    for j in range(N):
        if line[j] == 'J':
            r.append(i)
            c.append(j)

sq = [-1] * (N * N + 1)
for i in range(N + 1):
    sq[i * i] = i

l1 = []
l2 = []
pcnt = 0

for sum_val in range(N * N, 0, -1):
    for l in range(int(sum_val ** 0.5) + 1):
        if sq[sum_val - l * l] >= 0:
            l1.append(l)
            l2.append(sq[sum_val - l * l])
            pcnt += 1

ans = 0
ccnt = len(r)

for pi in range(pcnt):
    dr = l1[pi]
    dc = l2[pi]
    for ci in range(ccnt):
        r1 = r[ci] - dr
        c1 = c[ci] - dc
        if r1 < 0 or c1 < 0:
            continue
        if c[ci] + dr < N and r[ci] >= dr + dc:
            r2 = r1 - dc
            c2 = c1 + dr
            r3 = r2 + dr
            c3 = c2 + dc
            if map[r1][c1] != 'B' and map[r2][c2] != 'B' and map[r3][c3] != 'B':
                if (map[r1][c1] != 'J') + (map[r2][c2] != 'J') + (map[r3][c3] != 'J') <= 1:
                    ans = dr * dr + dc * dc
                    break
        if c[ci] >= dr + dc and r[ci] + dc < N:
            r2 = r1 + dc
            c2 = c1 - dr
            r3 = r2 + dr
            c3 = c2 + dc
            if map[r1][c1] != 'B' and map[r2][c2] != 'B' and map[r3][c3] != 'B':
                if (map[r1][c1] != 'J') + (map[r2][c2] != 'J') + (map[r3][c3] != 'J') <= 1:
                    ans = dr * dr + dc * dc
                    break
    if ans:
        break

print(ans)