import sys
input = sys.stdin.readline
import math

def init(li, tree, node, start, end):
    if start == end:
        tree[node] = li[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = (init(li, tree, node*2, start, mid) * init(li, tree, node*2+1, mid+1, end))
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
        tree[node] = (tree[node*2] * tree[node*2+1])

def product(tree, node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return (product(tree, node*2, start, mid, left, right) * product(tree, node*2+1, mid+1, end, left, right))

while(True):
    try:
        n, m = map(int, input().split())
    except Exception:
        break
    li = list(map(int, input().split()))

    for i in range(len(li)):
        if(li[i] < 0):
            li[i] = -1
        elif(li[i] > 0):
            li[i] = 1
    
    h = math.ceil(math.log2(n))
    tree_size = (1 << (h+1))
    tree = [1] * tree_size

    init(li, tree, 1, 0, n-1)

    res = []
    for _ in range(m):
        query = list(map(str, input().split()))
        if query[0] == 'C':
            t2, t3 = int(query[1]), int(query[2])

            if(t3 < 0):
                t3 = -1
            elif(t3 > 0):
                t3 = 1

            t2 -= 1
            li[t2] = t3
            update(tree, 1, 0, n-1, t2, t3)
        elif query[0] == 'P':
            t2, t3 = int(query[1]), int(query[2])
            ans = product(tree, 1, 0, n-1, t2-1, t3-1)
            if(ans == 0):
                res.append('0')
            elif(ans > 0):
                res.append('+')
            elif(ans < 0):
                res.append('-')
    
    for r in res:
        print(r, end="")
    print()