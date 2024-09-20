import sys
input = sys.stdin.readline

n, m = map(int, input().split())

max_edges = n * (n - 1) // 2
max_internal_edges = (n - 1) * (n - 2) // 2

if m >= max_edges:
    ans = n * (n - 1)
elif m <= n - 1:
    s = m + 1
    w_G1 = 2 * (s - 1) ** 2
    w_G2 = 2 * s * (n - s) * n
    w_G3 = (n - s) * (n - s - 1) * n
    ans = w_G1 + w_G2 + w_G3
else:
    m_remaining = m - (n - 1)
    max_internal_edges = (n - 1) * (n - 2) // 2
    edges_added = min(m_remaining, max_internal_edges)
    ans = 2 * (n - 1) ** 2 - 2 * edges_added
print(ans)