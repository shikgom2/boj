import sys
input = sys.stdin.readline

def update(tree, node, start, end, idx, diff):
    if end < idx or idx < start:
        return tree[node]
    elif start == end:
        tree[node] += diff
    else:
        mid = (start + end) // 2
        temp1 = update(tree, node * 2, start, mid, idx, diff)
        temp2 = update(tree, node * 2 + 1, mid + 1, end, idx, diff)
        tree[node] = temp1 + temp2
    return tree[node]

def query(tree, node, start, end, rank):
    if start == end:
        return start

    mid = (start + end) // 2
    left = tree[node * 2]
    if left >= rank:
        return query(tree, node * 2, start, mid, rank)
    return query(tree, node * 2 + 1, mid + 1, end, rank - left)

maxn = 1000001
n = int(input())
tree = [0] * (4 * maxn)
for _ in range(n):
    li = list(map(int, input().split()))
    if(li[0] == 1):
        k = query(tree, 1, 1, maxn, li[1])
        print(k)
        update(tree, 1, 1, maxn, k, -1)
    elif(li[0] == 2):
        update(tree, 1, 1, maxn, li[1], li[2])