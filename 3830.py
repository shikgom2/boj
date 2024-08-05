import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] == x:
        value[x] = 0
        return x
    y = find(parent[x])
    value[x] += value[parent[x]]
    parent[x] = y
    return y

def union(a, b, c):
    x, y = find(a), find(b)
    temp = value[a] - (value[b] - c)
    if(temp >= 0):
        parent[y] = x
        value[y] = abs(temp)
    else:
        parent[x] = y
        value[x] = abs(temp)

while(True):
    n,m = map(int, input().split())
    if(n==0 and m == 0):
        break

    parent = [i for i in range(n + 1)]
    value = [0] * (n+1)

    for _ in range(m):
        li = list(map(str, input().split()))

        if(li[0] == '!'):
            union(int(li[1]), int(li[2]), int(li[3]))
        elif(li[0] == '?'):
            if(find(int(li[1])) != find(int(li[2]))):
                print("UNKNOWN")
            else:
                print(value[int(li[2])] - value[int(li[1])])
                