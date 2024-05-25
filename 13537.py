import sys
input = sys.stdin.readline

class MergeSortTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [[] for _ in range(4 * self.n)]
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = [data[start]]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self.build(data, left_child, start, mid)
            self.build(data, right_child, mid + 1, end)
            
            self.tree[node] = self.merge(self.tree[left_child], self.tree[right_child])

    def merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    def query(self, L, R, k, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.count_greater(self.tree[node], k)
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_query = self.query(L, R, k, left_child, start, mid)
        right_query = self.query(L, R, k, right_child, mid + 1, end)

        return left_query + right_query

    def count_greater(self, sorted_list, k):
        low, high = 0, len(sorted_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_list[mid] <= k:
                low = mid + 1
            else:
                high = mid - 1
        return len(sorted_list) - low

n = int(input())
li = list(map(int, input().split()))
mst = MergeSortTree(li)

m = int(input())
for a in range(m):
    i,j,k = map(int, input().split())
    
    if(a >= 1):
        i = i ^ ans
        j = j ^ ans
        k = k ^ ans
    i -= 1
    j -= 1

    ans = mst.query(i,j,k)
    print(ans)