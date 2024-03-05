import sys
input = sys.stdin.readline

def lcp_array(s, suffix_array):
    n = len(s)
    lcp = [0] * n
    rank = [0] * n

    for i in range(n):
        rank[suffix_array[i]] = i

    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = suffix_array[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1

    return lcp

def suffix_array(s):

    n = len(s)
    sa = [i for i in range(n)]
    group = [ord(s[i]) for i in range(n)]
    new_group = [0] * (n + 1)

    group.append(-1)
    new_group[sa[0]] = 0
    new_group[n] = -1
    t = 1

    while t < n:
        sa.sort(key=lambda x: (group[x], group[min(x + t, n)]))

        for i in range(1, n):
            p, q = sa[i - 1], sa[i]
            if group[p] != group[q] or group[min(p + t, n)] != group[min(q + t, n)]:
                new_group[q] = new_group[p] + 1
            else:
                new_group[q] = new_group[p]

        if new_group[n - 1] == n - 1:
            break

        t = t * 2
        group = new_group[:]

    return sa

S = input().strip()
S += "$"
S2 = input().strip()

S += S2
suffix = suffix_array(S)

lcp = lcp_array(S, suffix)
#print(lcp)
max_ele = -1
max_idx = -1
for l in range(0, len(S)):
    if(lcp[l] > max_ele and lcp[l] <= min(len(S), len(S2))):
        max_ele = lcp[l]
        max_idx = l

if(max_idx < len(S2)):
    max_idx -= 1
    
print(max_idx)
print(S[suffix[max_idx] :])