import sys
input = sys.stdin.readline


n = int(input())
li = list(map(int, input().split()))

E = [0.0] * (n+1)
F = [0.0] * (n+1)

for i in range(1, n+1):
    k = li[i-1]
    low = i - k
    
    prev_sum = F[i-1] - (F[low-1] if low-1 >= 0 else 0)
    E[i] = 1 + prev_sum / k
    F[i] = F[i-1] + E[i]

print(E[n])