def can_see(H, i, j):
    dx = j - i
    dy = H[j] - H[i]
    for k in range(min(i, j) + 1, max(i, j)):
        val = dx * H[k] - dx * H[i] - dy * (k - i)
        if val * (1 if i < j else -1) >= 0:
            return False
    return True

def solve(H):
    N = len(H)
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i == j:
                continue
            if can_see(H, i, j):
                cnt += 1
        result = max(cnt, result)
    return result

N = int(input())
H = list(map(int, input().split()))

print(solve(H))