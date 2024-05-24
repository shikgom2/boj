import math
import sys
input = sys.stdin.readline

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        tree[node] = init(a, tree, node*2, start, (start+end)//2) + \
                     init(a, tree, node*2+1, (start+end)//2+1, end)
        return tree[node]

def update(tree, node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        update(tree, node*2, start, (start+end)//2, index, diff)
        update(tree, node*2+1, (start+end)//2+1, end, index, diff)

def sum(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return sum(tree, node*2, start, (start+end)//2, left, right) + sum(tree, node*2+1, (start+end)//2+1, end, left, right)

n = int(input())
a = [0] * n
for i in range(n):
    k = int(input())
    a[i] = k

h = math.ceil(math.log2(n))
tree_size = (1 << (h+1))
tree = [0] * tree_size

init(a, tree, 1, 0, n-1)

m = int(input())
ans = []
for _ in range(m):
    q = list(map(str, input().split()))
    if q[0] == 'U':
        t2, t3 = int(q[1]), int(q[2])
        t2 -= 1
        diff = t3
        a[t2] += t3
        update(tree, 1, 0, n - 1, t2, diff)
    elif q[0] == 'R':
        t2, t3 = int(q[1]), int(q[2])
        print(sum(tree, 1, 0, n-1, t2-1, t3-1))