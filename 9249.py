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

def find_lcs(S, S1_len, S2_len, suffix, lcp):
    max_len = -1
    index = -1
    
    for i in range(1, len(S)):
        # 현재 접미사와 이전 접미사가 서로 다른 문자열에서 온 경우
        if (suffix[i] < S1_len) != (suffix[i-1] < S1_len):
            if lcp[i-1] > max_len:
                max_len = lcp[i-1]
                index = suffix[i]
    
    if max_len > -1:
        return S[index:index+max_len]
    else:
        return "" 

S = input().strip()
S += "$"
S2 = input().strip()

S += S2
suffix = suffix_array(S)
lcp = lcp_array(S, suffix)

S1_len = len(S) - len(S2) - 1 
S2_len = len(S2)

lcs = find_lcs(S, S1_len, S2_len, suffix, lcp)
print(len(lcs))
print(lcs)