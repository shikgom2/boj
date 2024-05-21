import sys
input = sys.stdin.readline
import math
from collections import defaultdict

class Mo:
    def __init__(self, array, queries):
        self.array = array
        self.queries = queries
        self.block_size = int(math.sqrt(len(array)))
        self.results = [0] * len(queries)
        self.freq = defaultdict(int)
        self.current_unique_count = 0

    def add(self, idx):
        val = self.array[idx]
        if self.freq[val] == 0:
            self.current_unique_count += 1
        self.freq[val] += 1

    def remove(self, idx):
        val = self.array[idx]
        if self.freq[val] == 1:
            self.current_unique_count -= 1
        self.freq[val] -= 1

    def process_queries(self):
        queries = sorted(enumerate(self.queries), key=lambda x: (x[1][0] // self.block_size, x[1][1]))
        current_l, current_r = 0, 0
        
        for i, (l, r) in queries:
            while current_r <= r:
                self.add(current_r)
                current_r += 1
            while current_r > r + 1:
                current_r -= 1
                self.remove(current_r)
            while current_l < l:
                self.remove(current_l)
                current_l += 1
            while current_l > l:
                current_l -= 1
                self.add(current_l)
                
            self.results[i] = self.current_unique_count
        
        return self.results

n = int(input())
li = list(map(int, input().split()))
q = int(input())

queries = []
for _ in range(q):
    i, j = map(int, input().split())
    queries.append((i-1,j-1))

mo = Mo(li, queries)
ans = mo.process_queries()

for a in ans:
    print(a)