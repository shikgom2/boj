import math
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
    

n = int(input())
tree = BIT(1000001)

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

li = []
for i in range(n):
    li.append((li1[i], li2[i]))

li.sort(key= lambda x : (x[0], x[1]))
print(li)
ans = []
for i in range(len(li)):
    idx = li[i][1]
    ans.append(tree.range_query(idx+1, n))
    tree.update(idx, 1)

print(ans)