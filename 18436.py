import sys
input = sys.stdin.readline
import math

def init(a, even_tree, odd_tree, node, start, end):
    if start == end:
        even_tree[node] = 1 if a[start] % 2 == 0 else 0
        odd_tree[node] = 1 if a[start] % 2 != 0 else 0
        return even_tree[node], odd_tree[node]
    else:
        mid = (start + end) // 2
        left_even, left_odd = init(a, even_tree, odd_tree, node*2, start, mid)
        right_even, right_odd = init(a, even_tree, odd_tree, node*2+1, mid+1, end)
        even_tree[node] = left_even + right_even
        odd_tree[node] = left_odd + right_odd
        return even_tree[node], odd_tree[node]

def update(a, even_tree, odd_tree, node, start, end, index):
    if index < start or index > end:
        return even_tree[node], odd_tree[node]
    if start == end:
        even_tree[node] = 1 if a[start] % 2 == 0 else 0
        odd_tree[node] = 1 if a[start] % 2 != 0 else 0
        return even_tree[node], odd_tree[node]
    mid = (start + end) // 2
    left_even, left_odd = update(a, even_tree, odd_tree, node*2, start, mid, index)
    right_even, right_odd = update(a, even_tree, odd_tree, node*2+1, mid+1, end, index)
    even_tree[node] = left_even + right_even
    odd_tree[node] = left_odd + right_odd
    return even_tree[node], odd_tree[node]

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_result = query(tree, node*2, start, mid, left, right)
    right_result = query(tree, node*2+1, mid+1, end, left, right)
    return left_result + right_result

n = int(input())
li = list(map(int, input().split()))
h = math.ceil(math.log2(n))
tree_size = (1 << (h+1))
even_tree = [0] * tree_size
odd_tree = [0] * tree_size

init(li, even_tree, odd_tree, 1, 0, n-1)

m = int(input())
for _ in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        t2, t3 = q[1], q[2]
        t2 -= 1
        li[t2] = t3
        update(li, even_tree, odd_tree, 1, 0, n-1, t2)
    elif q[0] == 2:
        t2, t3 = q[1], q[2]
        even_count = query(even_tree, 1, 0, n-1, t2-1, t3-1)
        print(even_count)
    elif q[0] == 3:
        t2, t3 = q[1], q[2]
        odd_count = query(odd_tree, 1, 0, n-1, t2-1, t3-1)
        print(odd_count)