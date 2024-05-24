import sys
input = sys.stdin.readline
import math

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

n, m = map(int, input().split())
a = [0] * n 
h = math.ceil(math.log2(n))
tree_size = (1 << (h+1))
tree = [0] * tree_size

init(a, tree, 1, 0, n-1)

for _ in range(m):
    inputs = list(map(int, input().split()))
    if inputs[0] == 1:
        t2, t3 = inputs[1], inputs[2]
        t2 -= 1
        diff = t3
        a[t2] += t3
        update(tree, 1, 0, n-1, t2, diff)
    elif inputs[0] == 2:
        t2, t3 = inputs[1], inputs[2]
        print(sum(tree, 1, 0, n-1, t2-1, t3-1))
