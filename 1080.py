def flip(matrix, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrix[i][j] = '1' if matrix[i][j] == '0' else '0'

N, M = map(int, input().split())
A = [list(input().strip()) for _ in range(N)]
B = [list(input().strip()) for _ in range(N)]

if N < 3 or M < 3:
    print(0 if A == B else -1)
    exit()

ans = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(A, i, j)
            ans += 1

if A == B:
    print(ans)
else:
    print(-1)
