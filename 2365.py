import sys
input = sys.stdin.readline
from collections import deque

def edmond_karp(graph, source, sink, n):
    total_flow = 0
    while True:
        prev = [-1] * (2 * n + 2)
        queue = deque([(source, float('inf'))])

        while queue:
            cur, flow = queue.popleft()
            for nxt in range(2 * n + 2):
                if prev[nxt] == -1 and graph[cur][nxt] > 0: 
                    prev[nxt] = cur
                    new_flow = min(flow, graph[cur][nxt])
                    if nxt == sink:
                        total_flow += new_flow
                        while nxt != source:
                            cur = prev[nxt]
                            graph[cur][nxt] -= new_flow
                            graph[nxt][cur] += new_flow
                            nxt = cur
                        break
                    queue.append((nxt, new_flow))
            if prev[sink] != -1: 
                break
        
        if prev[sink] == -1:
            break

    return total_flow

n = int(input())
row = list(map(int, input().split()))
col = list(map(int, input().split()))

row_sum = sum(row)
left = 0
right = 10000

while True:
    mid = (left + right) // 2
    
    graph = [[0] * (2 * n + 2) for _ in range(2 * n + 2)]
    for i in range(n):
        graph[0][i + 1] = row[i]
        graph[n + i + 1][2 * n + 1] = col[i]

    for i in range(1, n + 1):
        for j in range(n + 1, 2 * n + 1):
            graph[i][j] = mid

    ans = edmond_karp(graph, 0, 2 * n + 1, n)

    if ans < row_sum:
        left = mid + 1
        if left > right:
            right = left
    else:
        right = mid - 1
        if left > right:
            print(mid)
            for j in range(1, n + 1):
                for i in range(n + 1, 2 * n + 1):
                    print(graph[i][j], end=' ')
                print()
            break