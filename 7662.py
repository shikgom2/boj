import sys
input = sys.stdin.readline
import heapq

n=int(input())
for _ in range(n):
    max_pq = []
    min_pq = []

    heapq.heapify(max_pq)
    heapq.heapify(min_pq)

    t = int(input())
    check = [True] * t

    for a in range(t):
        i, j = map(str, input().split())

        if(i == "I"):
            heapq.heappush(min_pq, (int(j), a)) #min
            heapq.heappush(max_pq, (int(j) * -1, a)) #max
            check[a] = True

        elif(i == "D"):
            if(j == "1"): #max

                while max_pq and check[max_pq[0][1]] == False:
                    heapq.heappop(max_pq)
            
                if(len(max_pq) != 0):
                    check[max_pq[0][1]] = True
                    _, idx = heapq.heappop(max_pq)
                    check[idx] = False

            elif(j == "-1"): #min

                while min_pq and check[min_pq[0][1]] == False:
                    heapq.heappop(min_pq)
            
                if(len(min_pq) != 0):
                    check[min_pq[0][1]] = True
                    _, idx = heapq.heappop(min_pq)
                    check[idx] = False

    while max_pq and check[max_pq[0][1]] == False:
            heapq.heappop(max_pq)
    while min_pq and check[min_pq[0][1]] == False:
            heapq.heappop(min_pq)

    if min_pq and max_pq:
        print(-max_pq[0][0],min_pq[0][0])
    else:
        print('EMPTY')