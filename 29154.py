import sys
input = sys.stdin.readline

def kmp(seq):
    n = len(seq)
    pi = [0] * n
    i = 1
    while i < n:
        j = pi[i - 1]
        while (j > 0) and (seq[i] != seq[j]):
            j = pi[j - 1]
        if seq[i] == seq[j]:
            j = j + 1
        pi[i] = j
        i = i + 1
    return pi


n,m = map(int, input().split())
s = list(map(int, input().split()))
l = list(map(int, input().split()))

p = []
i = len(l) - 1
while i >= 0:
    p.append(l[i])
    i = i - 1

text = []
i = len(s) - 1
while i >= 0:
    text.append(s[i])
    i = i - 1

sep = 0
s_combined = []
for element in p:
    s_combined.append(element)
s_combined.append(sep)
for element in text:
    s_combined.append(element)

ls_val = len(s_combined)

pi = kmp(s_combined)

lcp = [0] * n
base = m + 1
index = 0
while index < n:
    lcp[index] = pi[base + index]
    index = index + 1

diff = [0] * (n + 1)
j = 0
while j < n:
    k = lcp[j]
    if k > 0:
        pos = n - 1 - j
        start = pos - k + 1
        if start < 0:
            start = 0
        diff[start] = diff[start] + 1
        if pos + 1 < len(diff):
            diff[pos + 1] = diff[pos + 1] - 1
    j = j + 1

colored = [False] * n
curr = 0
i = 0
while i < n:
    curr = curr + diff[i]
    if curr > 0:
        colored[i] = True
    else:
        colored[i] = False
    i = i + 1

nim_sum = 0
i = 0
while i < n:
    if colored[i] is False:
        i = i + 1
        continue
    j = i
    while (j < n) and (colored[j] is True):
        j = j + 1
    length = j - i
    nim_sum = nim_sum ^ length
    i = j

if nim_sum != 0:
    print("First")
else:
    print("Second")