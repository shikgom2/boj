import math

MOD = 1000000007

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = (init(a, tree, node*2, start, mid) * init(a, tree, node*2+1, mid+1, end)) % MOD
        return tree[node]

def update(tree, node, start, end, index, value):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = value
    else:
        mid = (start + end) // 2
        update(tree, node*2, start, mid, index, value)
        update(tree, node*2+1, mid+1, end, index, value)
        tree[node] = (tree[node*2] * tree[node*2+1]) % MOD

def product(tree, node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return (product(tree, node*2, start, mid, left, right) * product(tree, node*2+1, mid+1, end, left, right)) % MOD

n, m, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))
tree_size = (1 << (h+1))
tree = [1] * tree_size

init(a, tree, 1, 0, n-1)

m += k
while m > 0:
    m -= 1
    inputs = list(map(int, input().split()))
    if inputs[0] == 1:
        t2, t3 = inputs[1], inputs[2]
        t2 -= 1
        a[t2] = t3
        update(tree, 1, 0, n-1, t2, t3)
    elif inputs[0] == 2:
        t2, t3 = inputs[1], inputs[2]
        print(product(tree, 1, 0, n-1, t2-1, t3-1))