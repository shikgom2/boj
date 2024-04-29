import sys; input = sys.stdin.readline

# 이분 매칭
def dfs(i):
    for j in graph[i]:
        if visited[j]: # 이미 고려한 열이면 넘어가자.
            continue
        visited[j] = True

        # 해당 열과 매칭된 행이 없거나 그 매칭된 행을 다시 매칭을 시도하여 성공할 경우
        if connect[j] == -1 or dfs(connect[j]):
            connect[j] = i
            return True

    # 모두 실패하면 매칭 실패
    return False

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 행 영역 별로 번호를 매긴다.
raw = [[0] * M for _ in range(N)]; ri = 0
is_open = False # 행이나 열이 이어지고 있는지 판별
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            if is_open:
                is_open = False
                ri += 1
        else:
            if not is_open:
                is_open = True
            raw[i][j] = ri
    if is_open:
        is_open = False
        ri += 1
print(raw)

# 열 영역 별로 번호를 매긴다.
col = [[0] * M for _ in range(N)]; ci = 0
for j in range(M):
    for i in range(N):
        if matrix[i][j] == 2:
            if is_open:
                is_open = False
                ci += 1
        else:
            if not is_open:
                is_open = True
            col[i][j] = ci
    if is_open:
        is_open = False
        ci += 1

print(col)
# 각 격자마다 빈 격자라면 행 영역에서 열 영역으로 이어지는 간선을 그래프에 추가
graph = [[] for _ in range(ri)]
for i in range(N):
    for j in range(M):
        if not matrix[i][j]:
            graph[raw[i][j]].append(col[i][j])

# 각 행 영역 별로 이분 매칭 시도
connect = [-1] * ci
result = 0
for i in range(ri):
    visited = [False] * ci
    if dfs(i):
        result += 1

print(result)