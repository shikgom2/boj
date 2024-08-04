import sys
input = sys.stdin.readline
from collections import deque

class deque_trick:
    def __init__(self):
        self.q = deque()
        self.dq = deque()

    def push(self, element):
        while self.dq and self.dq[-1][0] < element[0]:
            self.dq.pop()
        self.q.append(element)
        self.dq.append(element) 

    def pop(self):
        if self.q[0] == self.dq[0]:
            self.dq.popleft()
        self.q.popleft()

    def get_max(self):
        return self.dq[0][0]


n, m = map(int,input().split())

wall = []
for i in range(n):
    li = list(map(int, input().split()))
    wall.append(li)

r, s = map(int,input().split())

# Phase 1: Find max in each row within the window of width s
phase1 = [[-float('inf')] * (m - s + 1) for _ in range(n)]
for i in range(n):
    mq = deque_trick()
    for j in range(s - 1):
        mq.push((wall[i][j], j))
    for j in range(s - 1, m):
        mq.push((wall[i][j], j))
        phase1[i][j - s + 1] = mq.get_max()
        mq.pop()

# Phase 2: Find max in each column within the window of height r
phase2 = [[-float('inf')] * (m - s + 1) for _ in range(n - r + 1)]
for j in range(m - s + 1):
    mq = deque_trick()
    for i in range(r - 1):
        mq.push((phase1[i][j], i))
    for i in range(r - 1, n):
        mq.push((phase1[i][j], i))
        phase2[i - r + 1][j] = mq.get_max()
        mq.pop()

for row in phase2:
    print(' '.join(map(str, row)))
