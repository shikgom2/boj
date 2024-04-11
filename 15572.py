MOD = 1999

def matrix_mult(A, B):
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def matrix_pow(A, p):
    if p == 1:
        return A
    elif p % 2 == 0:
        B = matrix_pow(A, p // 2)
        return matrix_mult(B, B)
    else:
        B = matrix_pow(A, p - 1)
        return matrix_mult(A, B)

N, M = map(int, input().split())
A = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        A[i][j] = 1

result = matrix_pow(A, M)
print(sum(result[0]) % MOD)