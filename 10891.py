import sys
sys.setrecursionlimit(10**6)

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

'''
for i in range(len(BCC)):
    for edge in BCC[i]:
        print(f"({edge[0]},{edge[1]})", end=" ")
    print()
'''

check = [False] * (v+1)
for i in range(len(BCC)):
    if(len(BCC[i]) > 3):
        for j in range(len(BCC[i])):
            check[BCC[i][j][0]] = True 
            check[BCC[i][j][1]] = True 
        continue

    print(check)

    s = set()
    for j in range(len(BCC[i])):
        s.add(BCC[i][j][0])
        s.add(BCC[i][j][1])
    
    s = list(s)
    for j in range(len(s)):
        if(check[s[j]]):
            print("Not Cactus")
            exit()
        check[s[j]] = True

print("Cactus")
    
