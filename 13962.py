import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(u):
    global cnt
    in_[u] = cnt
    cnt += 1
    for c in children[u]:
        dfs(c)
    out_[u] = cnt

def update(pos, val):
    pos += 1
    while pos <= e:
        bit[pos] += val
        pos += pos & -pos

def sum(pos):
    s = 0
    while pos > 0:
        s += bit[pos]
        pos -= pos & -pos
    return s

def range_sum(l, r):
    return sum(r) - sum(l)
    
e = int(input())

manager = [0]*(e+1)
rank_ = [0]*(e+1)
review_time = [0]*(e+1)

root = -1
for i in range(1, e+1):
    m_i, r_i, t_i = map(int, input().split())
    manager[i] = m_i
    rank_[i] = r_i
    review_time[i] = t_i
    if m_i == -1:
        root = i

children = [[] for _ in range(e+1)]
for i in range(1, e+1):
    if manager[i] != -1:
        children[ manager[i] ].append(i)

in_ = [0]*(e+1)
out_ = [0]*(e+1)
cnt = 0

dfs(root)

bit = [0]*(e+1)

employees_sorted_by_rank = sorted(range(1, e+1), key=lambda x: rank_[x])

queries = []
for s in range(1, e+1):
    queries.append((rank_[s], in_[s], out_[s], s))
queries.sort(key=lambda x: x[0])


answers = [0]*(e+1)
emp_index = 0

for (r_s, in_s, out_s, s) in queries:
    while emp_index < e and rank_[ employees_sorted_by_rank[emp_index] ] < r_s:
        x = employees_sorted_by_rank[emp_index]
        update(in_[x], review_time[x])
        emp_index += 1
    
    answers[s] = range_sum(in_s, out_s)

# 7) 출력
for i in range(1, e+1):
    print(answers[i])
