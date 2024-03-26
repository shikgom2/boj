import heapq

N, K = map(int, input().split())
li = []
for _ in range(N):
    w, v = map(int, input().split())
    li.append((w, v))

bag = []
for _ in range(K):
    i = int(input())
    bag.append(i)

li.sort()
bag.sort()

res = 0
idx = 0
hq = []

for b in bag:
    while idx < N and li[idx][0] <= b:
        heapq.heappush(hq, -li[idx][1])
        idx += 1

    if hq:
        res += -heapq.heappop(hq) 

print(res)