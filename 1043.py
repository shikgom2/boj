import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

n,m = map(int, input().split())

know = list(map(int, input().split()))
del know[0]

if(len(know) == 0):
    print(m)
    exit()

ans = 0

parent = [i for i in range(n + 1)]

for _ in range(m):

    li = list(map(int, input().split()))
    del li[0]

    for i in range(len(li)):
        if(li[i] in know):
            for j in range(len(li)):
                if(li[i] != li[j]):
                    union(li[i], li[j])
    print(parent)

print(ans)