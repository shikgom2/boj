import sys
input = sys.stdin.readline
MAX_N = 10**7


pf_count = [0] * (MAX_N + 1)

for i in range(2, MAX_N + 1):
    if pf_count[i] == 0:
        for j in range(i, MAX_N + 1, i):
            pf_count[j] += 1

even_cum = [0] * (MAX_N + 1)
odd_cum = [0] * (MAX_N + 1)

for i in range(2, MAX_N + 1):
    even_cum[i] = even_cum[i-1]
    odd_cum[i] = odd_cum[i-1]
    if pf_count[i] % 2 == 0:
        even_cum[i] += 1
    else:
        odd_cum[i] += 1

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    even_count = even_cum[b] - even_cum[a-1]
    odd_count = odd_cum[b] - odd_cum[a-1]
    print(even_count - odd_count)