import sys
input = sys.stdin.readline

def manacher(s):
    A = '@#' + '#'.join(s) + '#$'
    Z = [0] * len(A)
    center = right = 0

    for i in range(1, len(A) - 1):
        if i < right:
            Z[i] = min(right - i, Z[2 * center - i])
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
        if i + Z[i] > right:
            center, right = i, i + Z[i]
    return Z

s = input()
arr = list(map(str, input().split()))
res = manacher(arr)
print(res)
N = int(input())

for _ in range(N):
    i,j = map(int, input().split())


    i = 2 * i + 2
    j = 2 * j + 2

    center = (i + j) // 2

    len = (i - j) // 2

    if res[center] >= len:
        print(1)
    else:
        print(0)