import sys
input = sys.stdin.readline

def init(li): 
    for i in range(n):  
        tree[n + i] = li[i] #initalize
    for i in range(n - 1, 0, -1):  #initalize next value
        tree[i] = min(tree[i << 1], tree[i << 1 | 1])

def update(idx, value):        
    tree[idx + n] = value #update value
    idx = idx + n
    i = idx; 
    while i > 1 :  #update value while down degree
        tree[i >> 1] = tree[i] + tree[i ^ 1];  
        i >>= 1;  

def query(l, r) :  
    res = 10**100
    l += n
    r += n 
    while l < r : 
        if (l & 1) : 
            res = min(res, tree[l])  
            l += 1
        if (r & 1) :
            r -= 1 
            res = min(res, tree[r])  
        l >>= 1 
        r >>= 1
    return res

n,m = map(int, input().split())
tree = [0] * (2 * n)

li = []
for _ in range(n):
    k = int(input())
    li.append(k)

init(li)
for _ in range(m):
    s,e = map(int, input().split())
    print(query(s-1,e))