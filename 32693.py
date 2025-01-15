import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

pairs = []
idx_map = {}
cnt_pairs = 0

for start in range(M):
    for end in range(start+1, M):
        length = end - start + 1
        if length % 2 == 0:
            idx_map[(start, end)] = cnt_pairs
            pairs.append((start, end))
            cnt_pairs += 1
pal = [[False]*(cnt_pairs) for _ in range(N)]

def manacher(s):
    n = len(s)
    d2 = [0]*n
    l, r = 0, -1
    for i in range(n):
        if i <= r:
            d2[i] = min(d2[l+r-i+1], r - i + 1)
        while i - d2[i] - 1 >= 0 and i + d2[i] < n \
              and s[i - d2[i] - 1] == s[i + d2[i]]:
            d2[i] += 1
        if i + d2[i] - 1 > r:
            l = i - d2[i]
            r = i + d2[i] - 1
    return d2

for i in range(N):
    row = grid[i]
    d2 = manacher(row)
    for center in range(M):
        radius = d2[center]
        for r in range(1, radius+1):
            start = center - r
            end = center + r - 1
            if (start, end) in idx_map:
                pal[i][ idx_map[(start, end)] ] = True

ans = 0
for idx, (c1, c2) in enumerate(pairs):
    left = 0
    for i in range(N):
        if pal[i][idx]:
            left += 1
        else:
            if left > 0:
                ans += left * (left + 1) // 2
            left = 0
    if left > 0:
        ans += left * (left + 1) // 2

print(ans)
