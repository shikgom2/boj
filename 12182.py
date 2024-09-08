import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def func(r, c, s, count, visited, a):
    visited[r][c] = True
    
    if r-1 >= 0:
        if a[r-1][c] == a[r][c] + 1:
            func(r-1, c, s, count, visited, a)
            count[r][c] += count[r-1][c]
    
    if c-1 >= 0:
        if a[r][c-1] == a[r][c] + 1:
            func(r, c-1, s, count, visited, a)
            count[r][c] += count[r][c-1]
    
    if r+1 < s:
        if a[r+1][c] == a[r][c] + 1:
            func(r+1, c, s, count, visited, a)
            count[r][c] += count[r+1][c]
    
    if c+1 < s:
        if a[r][c+1] == a[r][c] + 1:
            func(r, c+1, s, count, visited, a)
            count[r][c] += count[r][c+1]

t = int(input())

for j in range(1, t + 1):
    s = int(input())
    mp = {}
    a = []
    visited = [[False] * s for _ in range(s)]
    count = [[1] * s for _ in range(s)]
    
    for i in range(s):
        row = list(map(int, input().split()))
        a.append(row)
        for l in range(s):
            mp[a[i][l]] = (i, l)
    
    for i in range(1, s * s + 1):
        if not visited[mp[i][0]][mp[i][1]]:
            func(mp[i][0], mp[i][1], s, count, visited, a)
    
    ans = 1
    for i in range(2, s * s + 1):
        if count[mp[i][0]][mp[i][1]] > count[mp[ans][0]][mp[ans][1]]:
            ans = i
    
    print(f"Case #{j}: {ans} {count[mp[ans][0]][mp[ans][1]]}")