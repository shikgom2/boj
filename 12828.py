import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
k = int(input())
li = list(map(int, input().split()))

seg = []
max = 0
for row in board:
    len = 0
    for ch in row:
        if ch == '.':
            len += 1
        else:
            if len > 0:
                seg.append(len)
                if len > max:
                    max = len
                len = 0
    if len > 0:
        seg.append(len)
        if len > max:
            max = len

g = [0] * (max + 1)
F = [0] * (max + 1)
F[0] = 1

for l in range(1, max + 1):
    mask = 0
    for p in li:
        if p > l:
            break
        t = l - p
        mask |= F[t]
    mex = 0
    while mask & (1 << mex):
        mex += 1
    g[l] = mex
    mask = 0
    for i in range(l + 1):
        xor_val = g[i] ^ g[l - i]
        mask |= (1 << xor_val)
    F[l] = mask
    
nim_sum = 0
for seg in seg:
    nim_sum ^= g[seg]

if nim_sum != 0:
    print("nein")
else:
    print("hyo123bin")
