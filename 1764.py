import collections

N, M = map(int,input().split())
d = collections.defaultdict(int)

for _ in range(N + M):
    i = input()
    d[i] += 1
li = []

for key, val in d.items():
    if val == 2:
        li.append(key)
li.sort()
print(len(li))
for l in li:
    print(l)