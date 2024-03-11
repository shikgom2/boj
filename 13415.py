def solve(n, arr, k, ab):
    for i in range(k):
        a, b = ab[i]
        arr[:a] = sorted(arr[:a])
        arr[:b] = sorted(arr[:b], reverse=True)
    return arr

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
ab = [list(map(int, input().split())) for _ in range(k)]
print(*solve(n, arr, k, ab))