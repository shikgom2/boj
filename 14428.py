import sys
input = sys.stdin.readline
import math

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    else:
        mid = (start + end) // 2
        left_index = init(a, tree, node*2, start, mid)
        right_index = init(a, tree, node*2+1, mid+1, end)
        if a[left_index] < a[right_index] or (a[left_index] == a[right_index] and left_index < right_index):
            tree[node] = left_index
        else:
            tree[node] = right_index
        return tree[node]

def update(a, tree, node, start, end, index):
    if index < start or index > end:
        return tree[node]
    if start == end:
        return start
    mid = (start + end) // 2
    left_index = update(a, tree, node*2, start, mid, index)
    right_index = update(a, tree, node*2+1, mid+1, end, index)
    if a[left_index] < a[right_index] or (a[left_index] == a[right_index] and left_index < right_index):
        tree[node] = left_index
    else:
        tree[node] = right_index
    return tree[node]

def query(a, tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_index = query(a, tree, node*2, start, mid, left, right)
    right_index = query(a, tree, node*2+1, mid+1, end, left, right)
    if left_index == -1:
        return right_index
    if right_index == -1:
        return left_index
    if a[left_index] < a[right_index] or (a[left_index] == a[right_index] and left_index < right_index):
        return left_index
    else:
        return right_index

n = int(input())
a = list(map(int, input().split()))
h = math.ceil(math.log2(n))
tree_size = (1 << (h+1))
tree = [0] * tree_size

init(a, tree, 1, 0, n-1)

m = int(input())
while m > 0:
    m -= 1
    inputs = list(map(int, input().split()))
    if inputs[0] == 1:
        t2, t3 = inputs[1], inputs[2]
        t2 -= 1
        a[t2] = t3
        update(a, tree, 1, 0, n-1, t2)
    elif inputs[0] == 2:
        t2, t3 = inputs[1], inputs[2]
        ans = query(a, tree, 1, 0, n-1, t2-1, t3-1)
        print(ans + 1)