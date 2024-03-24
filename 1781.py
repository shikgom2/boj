import heapq

# 입력 받기
n = int(input())
ramen = []
for _ in range(n):
    first, second = map(int, input().split())
    ramen.append((first, second))

# ramen을 first 기준으로 정렬
ramen.sort()

# 우선순위 큐 초기화
pq = []
sum = 0

# 모든 ramen 요소에 대해 처리
for i in range(n):
    dl = ramen[i][0]
    # 우선순위 큐에 -second를 넣어 최대 힙처럼 동작하게 함
    heapq.heappush(pq, -ramen[i][1])

    # 조건을 만족하지 않을 때까지 우선순위 큐에서 제거
    while dl < len(pq):
        heapq.heappop(pq)

# 우선순위 큐에 남아 있는 모든 요소를 합산
while pq:
    sum += heapq.heappop(pq)

# 결과 출력
print(-sum)