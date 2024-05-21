import math
import sys
input = sys.stdin.readline
from typing import List, Tuple

sys.setrecursionlimit(100000)

def init(a: List[int], tree: List[Tuple[int, int]], node: int, start: int, end: int) -> Tuple[int, int]:
    if start == end:
        tree[node] = (a[start], a[start])
    else:
        mid = (start + end) // 2
        left = init(a, tree, node * 2, start, mid)
        right = init(a, tree, node * 2 + 1, mid + 1, end)
        tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
    return tree[node]

def findMinMax(tree: List[Tuple[int, int]], node: int, start: int, end: int, left: int, right: int) -> Tuple[int, int]:
    if left > end or right < start:
        return (sys.maxsize, -sys.maxsize - 1)
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    leftMinMax = findMinMax(tree, node * 2, start, mid, left, right)
    rightMinMax = findMinMax(tree, node * 2 + 1, mid + 1, end, left, right)
    return (min(leftMinMax[0], rightMinMax[0]), max(leftMinMax[1], rightMinMax[1]))

n, m = map(int, input().split())
a = []
for _ in range(n):
    k = int(input())
    a.append(k)

h = math.ceil(math.log2(n))
tree_size = (1 << (h + 1))
tree = [(0, 0)] * tree_size

init(a, tree, 1, 0, n - 1)

for _ in range(m):
    t1, t2 = map(int, input().split())
    ans = findMinMax(tree, 1, 0, n - 1, t1 - 1, t2 - 1)
    print(ans[1] - ans[0])
