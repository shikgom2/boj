import math
import sys
input = sys.stdin.readline

def init(li) : 
    for i in range(n) :  
        tree[n + i] = li[i];  
    for i in range(n - 1, 0, -1) :  
        tree[i] = tree[i << 1] + tree[i << 1 | 1];  

def update(idx, value):        
    tree[idx + n] = value;  
    idx = idx + n;  
    i = idx; 
    while i > 1 : 
        tree[i >> 1] = tree[i] + tree[i ^ 1];  
        i >>= 1;  

def query(l, r) :  
    res = 0;  
    l += n; 
    r += n; 
    while l < r : 
        if (l & 1) : 
            res += tree[l];  
            l += 1
        if (r & 1) :
            r -= 1; 
            res += tree[r];  
        l >>= 1; 
        r >>= 1
    return res;  

n = int(input())
tmp = list(map(int, input().split()))
li = []
for i in range(n):
    li.append((tmp[i], i))

tree = [0] * (2 * n)
li.sort()

ans = 0
for i in range(n):
    idx = li[i][1]
    ans += query(idx, n)
    update(idx, 1)
print(ans)