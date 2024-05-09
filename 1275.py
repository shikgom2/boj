import math

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        tree[node] = init(a, tree, node*2, start, (start+end)//2) + init(a, tree, node*2+1, (start+end)//2+1, end)
        return tree[node]

def update(tree, node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        update(tree, node*2, start, (start+end)//2, index, diff)
        update(tree, node*2+1, (start+end)//2+1, end, index, diff)

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return query(tree, node*2, start, (start+end)//2, left, right) + query(tree, node*2+1, (start+end)//2+1, end, left, right)

n, m = map(int, input().split())
a = list(map(int, input().split()))
h = math.ceil(math.log2(n))
tree_size = (1 << (h+1))
tree = [0] * tree_size

init(a, tree, 1, 0, n-1)

for _ in range(m):
    li = list(map(int, input().split()))

    t2, t3 = li[0], li[1]
    if(t2 > t3):
        t2, t3 = t3, t2
    print(query(tree, 1, 0, n-1, t2-1, t3-1))

    t2, t3 = li[2], li[3]
    t2 -= 1
    diff = t3 - a[t2]
    a[t2] = t3
    update(tree, 1, 0, n-1, t2, diff)