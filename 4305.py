#DFS
def dfs(graph, v, visited, stack):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited, stack)
    stack.append(v)

#Reverse DFS
def reverseDFS(graph, v, visited, component):
    visited[v] = True
    component.append(v) #Add SCC
    for w in graph[v]:
        if not visited[w]:
            reverseDFS(graph, w, visited, component)

def replace(s):
    replaced = [ord(letter) - 64 for letter in s]
    return replaced

def replace2(n):
    replaced = chr(n + 64) 
    return replaced

while(True):
    #input
    N = int(input())
    if(N == 0):
        break
    V = 26
    E = N * 4

    graph = [[] for _ in range(V + 1)]
    reverse_graph = [[] for _ in range(V + 1)]
    check = [0] * (V+1)
    #Init graph

    for i in range(N):
        s = list(map(str, input().split()))
        r = replace(s)

        for j in range(5):
            if(r[j] != r[5]):
                graph[r[j]].append(r[5])
                reverse_graph[r[5]].append(r[j])
                check[r[j]] += 1
        check[r[5]] += 1
    visited = [False] * (V + 1)
    stack = [] #DFS stack


    # DFS on original graph
    for i in range(1, V + 1):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    visited = [False] * (V + 1)
    results = []

    # Reverse DFS on reversed graph
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            reverseDFS(reverse_graph, node, visited, component)
            results.append(sorted(component))

    #Output
    cnt = 0
    for result in sorted(results):
        if(check[result[0]] == 0):
            continue
        cnt += 1
        for V in result:
            print(replace2(int(V)), end=' ')
        print("")
    print("")