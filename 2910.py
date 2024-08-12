import sys
input = sys.stdin.readline

n,c = map(int, input().split())
li = list(map(int, input().split()))

dir = {}
for i in range(len(li)):
    if li[i] not in dir:
        dir[li[i]] = 1
    else:
        dir[li[i]] += 1

dir = dict(sorted(dir.items(), key=lambda item: item[1], reverse=True))

for key, value in dir.items():
    for i in range(value):
        print(key, end=' ')
        