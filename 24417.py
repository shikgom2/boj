mod = 1000000007

def matrix_multiply(A, B):
    result = [[0, 0], [0, 0]]
    result[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod
    result[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod
    result[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod
    result[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod
    return result

def fibo(i):
    if i == 0:
        return [[1, 0], [0, 1]]
    elif i == 1:
        return [[1, 1], [1, 0]]
    else:
        t = fibo(i // 2)
        t = matrix_multiply(t, t)  # t^2
        if i % 2 == 1:
            t = matrix_multiply(t, [[1, 1], [1, 0]])
        return t

i = int(input())
result = fibo(i)
print(f'{result[0][1]} {(i-2) % mod}')