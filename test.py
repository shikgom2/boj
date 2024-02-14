import sys
from collections import deque
from queue import Queue

input = sys.stdin.readline

case = int(input())

for i in range(case):
    n, m = map(int, input().split())

    deq = deque(list(map(int, input().split())))

    index = Queue()
    for i in range(n):
        index.put(i)

    count = 1
    k = 10

    while True:
        brk = False
        for i in range(len(deq)):
            if deq[0] < deq[i]:
                brk = True
                deq.append(deq.popleft())
                index.put(index.get())
                break

        if not brk:
            deq.popleft()
            k = index.get()

            if k == m:
                break
            else:
                count += 1

    print(count)