import sys
input = sys.stdin.readline
from collections import deque

class deque_trick:
    def __init__(self):
        self.q = deque()
        self.dq = deque()

    def push(self, element):
        while self.dq and self.dq[-1][0] > element[0]:
            self.dq.pop()
        self.q.append(element)
        self.dq.append(element)

    def pop(self):
        if self.q[0] == self.dq[0]:
            self.dq.popleft()
        self.q.popleft()

    def get_element(self):
        return self.dq[0][0]

n, l = map(int, input().split())
pq = deque_trick()
li = list(map(int, input().split()))

for i in range(len(li)):
    if i >= l and pq.q[0][1] <= i - l:  # 윈도우 범위 밖의 요소 제거
        pq.pop()
    pq.push((li[i], i))  # (값, 인덱스) 형태로 push
    print(pq.get_element(), end=" ")
