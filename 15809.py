import sys
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def merge(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if a < b:
            root[b] = a
            li[a] += li[b]
        else:
            root[a] = b
            li[b] += li[a]

def fight(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if li[a] > li[b]:
            li[a] -= li[b]
            root[b] = a
        elif li[a] < li[b]:
            li[b] -= li[a]
            root[a] = b
        else:
            root[a] = 0
            root[b] = 0

n, m = map(int, input().split())
root = list(range(n + 1))
li = [0]
for _ in range(n):
    k = int(input())
    li.append(k)

for _ in range(m):
    o, p, q = map(int, input().split())
    if o == 1:
        merge(p, q)
    else:
        fight(p, q)

s = set()
for i in range(1, n + 1):
    p = find(i)
    if p != 0:
        s.add(p)

ans = sorted(li[p] for p in s)
print(len(s))
print(' '.join(map(str, ans)))
