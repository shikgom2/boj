def dfs(n):
    

n = int(input())

li = list(map(int, input().split()))

for i in range(len(li)):
    cur = li[i]

    ans = []
    ans.append(cur)

    for j in range(len(li)):
        if(cur % 3):
            cur *= 2
            if(cur in li):
                ans.append(cur)
                continue
            else:
                break 
        else:
            cur //= 3
            if(cur in li):
                ans.append(cur)
                continue
            else:
                break
        
    print(*ans)
        