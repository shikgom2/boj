import sys
import math
input = sys.stdin.readline

def init(a, tree, node, start, end):
    if start == end:
        tree[node][0] = a[start]
        tree[node][1] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        
        #set current node about parent node
        tree[node][0] = max(tree[node*2][0], tree[node*2+1][0])
        tree[node][1] = min(tree[node*2][1], tree[node*2+1][1])

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return float('-inf'), float('inf')
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    l = query(tree, node*2, start, mid, left, right)
    r = query(tree, node*2+1, mid+1, end, left, right)

    #set query
    return max(l[0], r[0]), min(l[1], r[1])

n, m = map(int, input().split())
li = []
for _ in range(n):
    k = int(input())
    li.append(k)
    
h = math.ceil(math.log2(n))
tree_size = (1 << (h + 1))
tree = [[0, 0] for _ in range(tree_size)]

init(li, tree, 1, 0, n-1)

for _ in range(m):
    a,b = map(int, input().split())
    ans = query(tree, 1, 0, n-1, a-1, b-1)
    print(ans[0]-ans[1])