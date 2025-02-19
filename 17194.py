import math
from bisect import bisect_left
import sys
input = sys.stdin.readline 

N = int(input())
A = list(map(int, input().split()))
Z = A.count(0)
if Z == 0 or Z == 2 * N:
    print(0)
    exit()

A0 = [i for i, a in enumerate(A) if a == 0]
Z_total = len(A0)

M = [A0[i] - i for i in range(Z_total)]
P = [0] * (Z_total + 1)
for i in range(Z_total):
    P[i+1] = P[i] + M[i]

def abs_sum_val(l, r, X):
    k = bisect_left(M, X, l, r)
    left_count = k - l
    sum_left = X * left_count - (P[k] - P[l])
    right_count = r - k
    sum_right = (P[r] - P[k]) - X * right_count
    return sum_left + sum_right

def cost_left(r, c):
    if r <= 0:
        return 0
    return abs_sum_val(0, r, c)

def cost_right(r, c):
    t = Z_total - r
    if t <= 0:
        return 0
    
    d = (r / t) * c
    X_val = d - (r - N)
    return abs_sum_val(r, Z_total, X_val)

def total_cost(r, c):
    return cost_left(r, c) + cost_right(r, c)

ans = 10**20
r_min = max(0, Z_total - N)
r_max = min(Z_total, N)
for r in range(r_min, r_max + 1):
    t = Z_total - r 
    s = set()
    if r == 0 or t == 0:
        s.add(0)
    else:
        if r > 0:
            if r % 2 == 1:
                med = M[r // 2]
                s.add(med)
                s.add(med - 1)
                s.add(med + 1)
            else:
                med1 = M[r // 2 - 1]
                med2 = M[r // 2]
                cand = (med1 + med2) // 2
                s.add(med1)
                s.add(med2)
                s.add(cand)
                s.add(cand - 1)
                s.add(cand + 1)
        if t > 0 and r > 0:
            if t % 2 == 1:
                med_R = M[r + t // 2] + (r - N)
                cand = (t / r) * med_R
                s.add(math.floor(cand))
                s.add(math.ceil(cand))
            else:
                med_R1 = M[r + t // 2 - 1] + (r - N)
                med_R2 = M[r + t // 2] + (r - N)
                cand1 = (t / r) * med_R1
                cand2 = (t / r) * med_R2
                s.add(math.floor(cand1))
                s.add(math.ceil(cand1))
                s.add(math.floor(cand2))
                s.add(math.ceil(cand2))
        s.add(0)
    for c in s:
        cur = total_cost(r, c)
        if cur < ans:
            ans = cur

print(int(round(ans)))
