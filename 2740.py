N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M2, K = map(int, input().split()) 

B = [list(map(int, input().split())) for _ in range(M2)]

C = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        temp = 0
        for r in range(M):
            temp += A[i][r] * B[r][j]
        C[i][j] = temp

for row in C:
    print(*row)
