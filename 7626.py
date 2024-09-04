import sys
input = sys.stdin.readline 
import bisect

import sys
import bisect

input = sys.stdin.readline

INF = 10**10
mn = 200001

def update(node, ns, ne, l, r, val):
    if r < ns or ne < l:
        return
    if l <= ns and ne <= r:
        cnt[node] += val
    else:
        mid = (ns + ne) // 2
        update(node * 2, ns, mid, l, r, val)
        update(node * 2 + 1, mid + 1, ne, l, r, val)
    
    if cnt[node]:
        tree[node] = values[ne] - values[ns - 1]
    else:
        if ns == ne:
            tree[node] = 0
        else:
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

tree = [0] * (mn * 8)
cnt = [0] * (mn * 8)
lines = []
values = []

n = int(input())
for _ in range(n):
    x1, x2, y1, y2 = map(int, input().split())
    lines.append((x1, y1, y2, 1))
    lines.append((x2, y1, y2, -1))
    values.append(y1)
    values.append(y2)

values = sorted(set(values))  # Remove duplicates and sort

lines.sort()  # Sort by x

ans = 0
prev_x, prev_y1, prev_y2, prev_start = lines[0]
for i in range(2 * n):
    cur_x, cur_y1, cur_y2, cur_start = lines[i]
    dx = cur_x - prev_x
    ans += dx * tree[1]

    l = bisect.bisect_left(values, cur_y1)
    r = bisect.bisect_left(values, cur_y2)
    update(1, 1, len(values) - 1, l + 1, r, cur_start)
    prev_x, prev_y1, prev_y2, prev_start = cur_x, cur_y1, cur_y2, cur_start

print(ans)
