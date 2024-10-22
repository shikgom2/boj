import sys
input = sys.stdin.readline

from collections import deque

def bfs(x):
    q = deque([(x, 0)])
    ans = []
    visited[x] = True
    
    while q:
        idx, t = q.popleft()
        for i in graph[idx]:
            if not visited[i]:
                q.append((i, t+1))
                visited[i] = True
                ans.append(i)
                
    return ans

n = int(input()) 
dic = {}
reverse_dic = {}  
dic["Baba"] = 0
reverse_dic[0] = "Baba"  
idx = 1

graph = [[] for _ in range(1000001)]

for _ in range(n):
    s = input().split()

    if s[0] not in dic:
        dic[s[0]] = idx
        reverse_dic[idx] = s[0]  # 역방향 딕셔너리에 저장
        idx += 1
        source = dic[s[0]]
    else:
        source = dic[s[0]]
    
    if s[2] not in dic:
        dic[s[2]] = idx
        reverse_dic[idx] = s[2]  # 역방향 딕셔너리에 저장
        idx += 1
        target = dic[s[2]]
    else:
        target = dic[s[2]]
    
    graph[source].append(target)

visited = [False] * (n+1)
ans = bfs(0)

res = []
for i in ans:
    res.append(reverse_dic[i])  
    
res.sort()
for i in res:
    print(i)
