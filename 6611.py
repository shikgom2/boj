import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

while True:
    try:
        n, m = map(int, input().split())
        if n < 0 or m < 0:
            break
    except EOFError:
        break

    edges = []
    for _ in range(m):
        a, b, w = map(int, input().split())
        edges.append((w, a-1, b-1))

    parent = [i for i in range(n)]
    edges.sort()

    ans = 0
    size = 0

    replw = [[-1] * (n) for _ in range(n)]
    for i in range(n):
        replw[i][i] = 0

    for edge in edges:
        z, x, y = edge
        if find(x) != find(y):
            union(x, y)
            ans += z
            size += 1
            for i in range(n):
                for j in range(n):
                    if replw[i][x] != -1 and replw[j][y] != -1:
                        replw[j][i] = replw[i][j] = max(replw[i][x], max(w, replw[j][y]))

    if(size < n-1):
        print("disconnected")
    else:
        result = ans
        for w, x, y in edges:
            max_path_weight = max(replw[x][y], replw[y][x]) if replw[x][y] != -1 else 0
            temp_weight = ans - w + max_path_weight
            if temp_weight < result:
                result = temp_weight

        print(result)
