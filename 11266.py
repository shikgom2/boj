import sys
sys.setrecursionlimit(155757)

SIZE = 10001
graph = [[] for _ in range(SIZE)]
DFS_num = [0] * SIZE
DFS_min = [0] * SIZE
DFS_cnt = 1
stk = []
BCC = []

def add_edge(a, b):
    graph[a].append(b)
    graph[b].append(a)

def DFS(v, p):
    global DFS_cnt
    DFS_num[v] = DFS_min[v] = DFS_cnt
    DFS_cnt += 1

    for nv in graph[v]:
        if nv == p:
            continue
        if DFS_num[v] > DFS_num[nv]:
            stk.append((v, nv))

        if DFS_num[nv]:
            # Backward edge
            DFS_min[v] = min(DFS_min[v], DFS_num[nv])
        else:
            # Forward edge
            DFS(nv, v)
            DFS_min[v] = min(DFS_min[v], DFS_min[nv])

            if DFS_min[nv] >= DFS_num[v]:
                bcc = []
                while True:
                    e = stk.pop()
                    bcc.append(e)
                    if e == (v, nv):
                        break
                BCC.append(bcc)

def find_bcc(v):
    for i in range(1, v + 1):
        if not DFS_num[i]:
            DFS(i, 0)

v, e = map(int, input().split())

for _ in range(e):
    a, b = map(int, input().split())
    add_edge(a, b)
find_bcc(v)

ans = set()
check = [False] * (v+1)

for i in range(len(BCC)):
    tmp = set()
    for j in range(len(BCC[i])):
        for k in range(2):
            tmp.add(BCC[i][j][k])

    tmp = list(tmp)
    for j in range(len(tmp)):
        if(check[tmp[j]]):
            ans.add(tmp[j])
        else:
            check[tmp[j]] = True
            
ans = list(ans)
print(len(ans))
ans.sort()
print(*ans)