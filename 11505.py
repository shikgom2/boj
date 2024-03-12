import sys
input = sys.stdin.readline
MOD = 1000000007

class SegmentTree:
    def __init__(self, n, array):
        self.n = n
        self.array = array
        self.tree = [0] * (4*n)
        self.init(0,n-1,1)

    def init(self, left, right, idx):
        if left == right:
            self.tree[idx] = self.array[left] % MOD
            return self.tree[idx] % MOD
        mid = (left + right) // 2
        self.tree[idx] = (self.init(left, mid, 2*idx) * self.init(mid+1, right, 2*idx+1)) % MOD
        return self.tree[idx]

    def query(self, left, right, idx, node_left, node_right):
        if node_right < left or right < node_left:
            return 1
        if left <= node_left and node_right <= right:
            return self.tree[idx]
        mid = (node_left+node_right) // 2
        return( self.query(left, right, 2*idx, node_left, mid) * self.query(left, right, 2*idx+1, mid+1, node_right) ) % MOD

    def update(self, index, new_value, node_idx, node_left, node_right):
        if index < node_left or index > node_right:
            return self.tree[node_idx]
        if node_left == node_right:
            self.tree[node_idx] = new_value % MOD
            return self.tree[node_idx] % MOD
        mid = (node_left+node_right) // 2
        self.tree[node_idx] = (self.update(index, new_value, 2*node_idx, node_left, mid) * self.update(index, new_value, 2*node_idx+1, mid+1, node_right)) % 1000000007
        return self.tree[node_idx]

    def find_prod(self, left, right):
        return self.query(left, right, 1, 0, self.n-1)

    def update_value(self, index, value):
        return self.update(index, value, 1, 0, self.n-1)

n, m, k = map(int,input().split())
nums = [int(input()) for _ in range(n)]
segment_tree = SegmentTree(n, nums)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    
    if a == 1:
        segment_tree.update_value(b-1, c)
    else:
        print(segment_tree.find_prod(b-1,c-1))