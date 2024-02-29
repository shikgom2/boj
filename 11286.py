import heapq
import sys
input = sys.stdin.readline

N = int(input())
pq = []
pq_abs = []

for _ in range(N):
	num = int(input())
	num_abs = abs(num)
	if num != 0:
		heapq.heappush(pq, num)
		heapq.heappush(pq_abs, num_abs)
	elif num == 0:
		try:
			A = heapq.heappop(pq_abs)
			try:
					pq.remove(-A)
					print(-A)
			except:
					pq.remove(A)
					print(A)
		except:
			print(0)