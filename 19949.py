import sys
input = sys.stdin.readline
sys.setrecursionlimit(155557)

def dfs(idx):
    global cnt
    if idx == 10:
        s = 0
        for j in range(10):
            if li[j] == ans[j]:
                s += 1
        if s >= 5:
            cnt += 1
        return
    
    
    for i in range(1, 6):
        if idx > 1 and li[idx-2] == li[idx-1] == i:
            continue
        li.append(i)
        dfs(idx+1)
        li.pop()
    
ans = list(map(int, input().split()))
li, cnt = [], 0
dfs(0)
print(cnt)