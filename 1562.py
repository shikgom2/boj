MAX = 1023
INF = 10**9

def solve(start, idx, state):
    if idx == N - 1:
        return 1 if state == MAX else 0
    
    ret = cache[start][idx][state]
    if ret != -1:
        return ret
    
    ret = 0
    for i in range(2):
        next_start = start + dx[i]
        if next_start == 10 or next_start == -1:
            continue
        ret += solve(next_start, idx + 1, state | (1 << next_start))
        ret %= INF
    
    cache[start][idx][state] = ret
    return ret

N = int(input())

dx = [1, -1]
cache = [[[-1 for _ in range((1 << 10) + 1)] for _ in range(101)] for _ in range(11)]

ans = 0
for i in range(1, 10):
    ans += solve(i, 0, 1 << i)
    ans %= INF

print(ans)