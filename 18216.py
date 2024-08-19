import heapq

def dij(n, lengths, values):
    # Initialize priority queue and dp table
    pq = []
    dp = [[float('inf')] * 121 for _ in range(n + 1)]
    visited = [[False] * 121 for _ in range(n + 1)]
    
    # Set initial conditions for the priority queue
    for i in range(1, n + 1):
        dp[i][lengths[i]] = lengths[i]
        heapq.heappush(pq, (lengths[i], i, lengths[i]))  # (length, node index, current distance)
    
    # Process the queue
    while pq:
        _l, _w, _dis = heapq.heappop(pq)
        if _dis == 0:
            return _l
        if visited[_w][_dis]:
            continue
        visited[_w][_dis] = True
        pre = values[_w] & ((1 << _dis) - 1)
        
        # Check each possible node
        for i in range(1, n + 1):
            if i == _w and _dis == lengths[_w]:
                continue
            if _dis >= lengths[i]:
                tmp = pre >> (_dis - lengths[i])
                if tmp != values[i]:
                    continue
                dw, ddis, dl = _w, _dis - lengths[i], _l
            else:
                tmp = values[i] >> (lengths[i] - _dis)
                if tmp != pre:
                    continue
                dw, ddis, dl = i, lengths[i] - _dis, _l + (lengths[i] - _dis)
            
            if dp[dw][ddis] > dl:
                dp[dw][ddis] = dl
                heapq.heappush(pq, (dl, dw, ddis))
    
    return 0

n = int(input())
lengths = [0] * (n + 1)
values = [0] * (n + 1)

for i in range(1, n + 1):
    st = input().strip()
    lengths[i] = len(st)
    for ch in st:
        values[i] = (values[i] << 1) + int(ch)

print(dij(n, lengths, values))
