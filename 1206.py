N = int(input())
a_list = []
for _ in range(N):
    a = input()
    a_list.append(float(a))

def compute_min_M(t_j):
    t_j = int(t_j)
    max_n = 100000
    for n in range(1, max_n + 1):
        if t_j == 0:
            m_lower = 1
            m_upper = ( ( n + 1 ) * 10000 - 1 ) // ( t_j + 1 )
        else:
            m_lower = ( (n - 1) * 100000 ) // t_j + 1
            m_lower = max(m_lower, ( n * 100000 + t_j ) // ( t_j + 1 ) )
            m_upper = min( ( n * 100000 ) // t_j, ( ( n + 1 ) * 100000 - 1 ) // ( t_j + 1 ) )
        if m_lower <= m_upper:
            return m_lower
    return None  # Should not happen

max_M = 1
for a in a_list:
    t_j = int(round(a * 100000 + 1e-8))
    min_M_j = compute_min_M(t_j)
    if min_M_j is None:
        print("No solution found")
        exit()
    if min_M_j > max_M:
        max_M = min_M_j

print(max_M)
