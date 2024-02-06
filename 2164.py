from collections import deque

i = int(input())

queue = []
deque = deque(queue)

for a in range(1, i+1):
    deque.append(a)

#print(deque)

while(len(deque) != 1):
    k = deque.popleft()
    k = deque.popleft()
    deque.append(k)
    #print(deque)

print(deque[0])