import math
mod = 1000000000

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

if(i > 0):
    print("1")
elif(i == 0):
    print("0")
elif(i < 0 and (i+1) % 2 == 1):
    print("-1")
elif(i < 0 and (i+1) %2 == 0):
    print("1")
    i = i * -1

i = abs(i)
result = fibo(i)
print(result[0][1])
