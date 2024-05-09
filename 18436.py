import math

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = min(init(a, tree, node*2, start, mid), init(a, tree, node*2+1, mid+1, end))
        return tree[node]

def update(tree, node, start, end, index, value):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = value
        return
    mid = (start + end) // 2
    update(tree, node*2, start, mid, index, value)
    update(tree, node*2+1, mid+1, end, index, value)
    tree[node] = min(tree[node*2], tree[node*2+1])

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return float('inf')
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(query(tree, node*2, start, mid, left, right), query(tree, node*2+1, mid+1, end, left, right))

n = int(input())
a = list(map(int, input().split()))
h = math.ceil(math.log2(n))
tree_size = (1 << (h+1))
tree = [0] * tree_size

init(a, tree, 1, 0, n-1)

m = int(input())
for _ in range(m):
    li = list(map(int, input().split()))

    if(li[0] == 1):
        t2, t3 = li[1], li[2]
        t2 -= 1
        diff = t3 - a[t2]
        a[t2] = t3
        update(tree, 1, 0, n-1, t2, diff)
    elif(li[0] == 2):
        t2, t3 = li[1], li[2]
        if(t2 > t3):
            t2, t3 = t3, t2
        print(query(tree, 1, 0, n-1, t2-1, t3-1))
