import math
import sys
input = sys.stdin.readline

def update(tree, node, start, end, index, val):
    #out of range
    if index < start or index > end:
        return
    
    #add or update?
    if start == end:
        tree[node] += val    
        return
        
    update(tree, node*2, start, (start+end)//2, index, val)
    update(tree, node*2+1, (start+end)//2+1, end, index, val)
    
    tree[node] = tree[node*2] + tree[node*2+1]
        
def query(tree, node, start, end, left, right):
    #if out of range, how to return?
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
        
    l = query(tree, node*2, start, (start+end)//2, left, right)
    r = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    
    #how to return?
    return l + r   

t = int(input())
for ttt in range(t):
    n,m,k = map(int, input().split())

    ans = 0
    tree = [0] * 4001

    li = []
    for _ in range(k):
        a,b = map(int, input().split())
        li.append((a,b))

    li.sort(key= lambda x : (x[0], x[1]))
    for i in range(k):
        idx = li[i][1]
        ans += query(tree, 1, 0, m-1, idx, m-1)
        update(tree, 1, 0, m-1, idx-1, 1)

    print(f"Test case {ttt+1}: {ans}")