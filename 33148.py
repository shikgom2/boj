
import math
from collections import Counter
import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())
li = list(map(int, input().split()))

freq = Counter(li)
heap = list(freq.keys())
heapq.heapify(heap)

smallest = heap[0]
a0 = math.isqrt(smallest)
if a0 * a0 != heap[0]:
    print("NO")

ans = [a0]
freq[smallest] -= 1

cnt = Counter(ans)
needed = 0

for _ in range(1, n):
    while heap and freq[heap[0]] == 0:
        heapq.heappop(heap)
    if not heap:
        print("NO")
        exit()
    can = heap[0]
    if can % ans[0] != 0:
        print("NO")
        exit()
    can = can // ans[0]
    
    valid = True
    for v, count in list(cnt.items()):
        prod = v * can
        
        if v == can:
            needed += 1
        if freq[prod] < needed:
            valid = False
            break
    if not valid:
        print("nO")
        exit()
    
    for v, count in list(cnt.items()):
        prod = v * can
        dec = 2 * count
        if v == can:
            dec += 1
        freq[prod] -= dec
    ans.append(can)
    cnt[can] += 1
    
print("YES")
print(" ".join(map(str, ans)))
