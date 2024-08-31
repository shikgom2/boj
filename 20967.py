import sys
input = sys.stdin.readline
from collections import defaultdict

s = input().strip()

m = {}
for c in s:
    if c not in m:
        m[c] = 0

cnt = 0
for key in m:
    m[key] = cnt
    cnt += 1

N = len(m)

# Step 2: Create the occurrence matrix
oc = [[0] * len(m) for _ in range(len(m))]
for i in range(len(s) - 1):
    oc[m[s[i]]][m[s[i + 1]]] += 1

# Step 3: Initialize dp arrays
dp = [float('inf')] * (1 << N)
dp[0] = 1
bits = N // 2

# Step 4: Initialize stor1 and stor2
stor1 = [[0] * N for _ in range(1 << bits)]
stor2 = [[0] * N for _ in range(1 << (N - bits))]

# Step 5: Populate stor1 and stor2
for j in range(N):
    for i in range(1 << bits):
        for k in range(bits):
            if i & (1 << k):
                stor1[i][j] += oc[k][j]
    for i in range(1 << (N - bits)):
        for k in range(N - bits):
            if i & (1 << k):
                stor2[i][j] += oc[bits + k][j]

# Step 6: Compute the dp array
for i in range(1 << N):
    for j in range(N):
        if i & (1 << j):
            sum_ = dp[i ^ (1 << j)]
            sum_ += stor1[i & ((1 << bits) - 1)][j]
            sum_ += stor2[i >> bits][j]
            dp[i] = min(dp[i], sum_)


print(dp[(1 << N) - 1])