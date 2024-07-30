import sys
import re
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    for u in range(1, n + 1):
        if pair_u[u] == 0:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')
    
    dist[0] = float('inf')
    while queue:
        u = queue.popleft()
        if dist[u] < dist[0]:
            for v in graph[u]:
                if dist[pair_v[v]] == float('inf'):
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
    return dist[0] != float('inf')

def dfs(u):
    if u != 0:
        for v in graph[u]:
            if dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v]):
                pair_v[v] = u
                pair_u[u] = v
                return True
        dist[u] = float('inf')
        return False
    return True

def extract_numbers(s):
    s = ''.join(s)
    
    before_colon = re.search(r'(\d+):', s)
    if before_colon:
        num_before_colon = int(before_colon.group(1))
    else:
        num_before_colon = None
    
    after_parenthesis = re.findall(r'\)\s*(\d+(?:\s+\d+)*)', s)
    nums_after_parenthesis = []
    if after_parenthesis:
        nums_after_parenthesis = list(map(int, after_parenthesis[0].split()))

    return num_before_colon, nums_after_parenthesis

V = 20001

while(True):
    graph = [[] for _ in range(V+1)]
    d = [0] * (V+1)
    try:
        n = int(input())
    except Exception:
        break

    for i in range(1, n + 1):
        li = list(map(str, input().rstrip()))
        s, num_li = extract_numbers(li)
        #print(s, num_li)
        for j in range(len(num_li)):
            graph[s+1].append(num_li[j] + 1)

    pair_u = [0] * (V + 1)
    pair_v = [0] * (V + 1)
    dist = [0] * (V + 1)

    ans = 0
    while bfs():
        for u in range(1, n + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    ans += 1

    print(ans)