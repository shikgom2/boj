import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())

li = [0] * N
li[0] = 1
cur = 0
ans = 0

if li[0] == M:
    print(0)
    exit()
        
while True:
    if li[cur] % 2 == 1:
        nx = (cur + L) % N
    else:
        nx = (cur - L) % N

    cur = nx
    li[cur] += 1
    ans += 1

    if li[cur] == M:
        break

print(ans)