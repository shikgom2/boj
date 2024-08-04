import sys
input = sys.stdin.readline

class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)
    
n, m, k = map(int, input().split())

tree = BIT(n)
li = [0]
for i in range(n):
    a = int(input())
    tree.update(i+1, a)
    li.append(a)

m += k
for _ in range(m):
    a,b,c = map(int ,input().split())
    if(a == 1): #upadte
        delta = c - li[b]
        tree.update(b, delta)
        li[b] = c
    else: #query
        print(tree.range_query(b, c))
