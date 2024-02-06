mod = 1000

def matrix_multiply(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= mod
    return result

def solve(A, B, N):
    if B == 1:
        return [[element % mod for element in row] for row in A]
    if B % 2 == 0:
        half = solve(A, B//2, N)
        return matrix_multiply(half, half, N)
    else:
        half = solve(A, B//2, N)
        return matrix_multiply(matrix_multiply(half, half, N), A, N)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = solve(A, B, N)
for row in result:
    print(' '.join(map(str, row)))