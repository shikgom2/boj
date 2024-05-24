import math
import sys
input = sys.stdin.readline

def init(a, tree, lazy, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        tree[node] = init(a, tree, lazy, node*2, start, (start+end)//2) + \
                     init(a, tree, lazy, node*2+1, (start+end)//2+1, end)
        return tree[node]

def update_lazy(tree, lazy, node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update_range(tree, lazy, node, start, end, l, r, diff):
    update_lazy(tree, lazy, node, start, end)
    if l > end or r < start:
        return
    if l <= start and end <= r:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    update_range(tree, lazy, node*2, start, (start+end)//2, l, r, diff)
    update_range(tree, lazy, node*2+1, (start+end)//2+1, end, l, r, diff)
    tree[node] = tree[node*2] + tree[node*2+1]

def sum_lazy(tree, lazy, node, start, end, l, r):
    update_lazy(tree, lazy, node, start, end)
    if l > end or r < start:
        return 0
    if l <= start and end <= r:
        return tree[node]
    return sum_lazy(tree, lazy, node*2, start, (start+end)//2, l, r) + \
           sum_lazy(tree, lazy, node*2+1, (start+end)//2+1, end, l, r)

n, m, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))
tree_size = (1 << (h+1))
tree = [0] * tree_size
lazy = [0] * tree_size

init(a, tree, lazy, 1, 0, n-1)

m += k
for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        t2, t3, t4 = query[1], query[2], query[3]
        update_range(tree, lazy, 1, 0, n-1, t2-1, t3-1, t4)
    elif query[0] == 2:
        t2, t3 = query[1], query[2]
        print(sum_lazy(tree, lazy, 1, 0, n-1, t2-1, t3-1))