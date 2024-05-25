import sys
input = sys.stdin.readline
from math import sqrt

mem = 100007

class Query:
    def __init__(self, l, r, idx):
        self.l = l
        self.r = r
        self.idx = idx

    def __lt__(self, other):
        if self.l // sq == other.l // sq:
            return self.r < other.r if (self.l // sq) % 2 == 0 else self.r > other.r
        return self.l // sq < other.l // sq

def add(x):
    global max_count, max_freq_number
    freq[x] += 1
    cnt[freq[x]] += 1
    if freq[x] > max_count:
        max_count = freq[x]
        max_freq_number = x
    elif freq[x] == max_count:
        if x < max_freq_number:
            max_freq_number = x

def sub(x):
    global max_count, max_freq_number
    cnt[freq[x]] -= 1
    if cnt[freq[x]] == 0 and max_count == freq[x]:
        max_count -= 1
        for i in range(len(freq)):
            if freq[i] == max_count:
                max_freq_number = i
                break
    freq[x] -= 1
    if freq[x] == max_count and x < max_freq_number:
        max_freq_number = x

n, k = map(int, input().split())
li = list(map(int, input().split()))
sq = int(sqrt(n))
m = int(input())
query = []
w = []
for i in range(m):
    q1, q2 = map(int, input().split())
    query.append(Query(q1 - 1, q2 - 1, i))
    w.append(q2-q1+1)
query.sort()

ans = [0] * m
freq = [0] * (max(li) + 1)
cnt = [0] * (n + 1)
max_count = 0
max_freq_number = -1

s, e = 0, 0
add(li[0])

for q in query:
    while e < q.r:
        e += 1
        add(li[e])
    while e > q.r:
        sub(li[e])
        e -= 1
    while s < q.l:
        sub(li[s])
        s += 1
    while s > q.l:
        s -= 1
        add(li[s])
    ans[q.idx] = (max_freq_number, max_count)

for i in range(len(ans)):
    #print("human : " ,w[i], "ans : " , ans[i][1])
    if(w[i] // 2 < ans[i][1]):
        print(f"yes {ans[i][0]}")
    else:
        print("no")
