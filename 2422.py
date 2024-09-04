import sys
input = sys.stdin.readline

li = []
n,m=map(int, input().split())
for _ in range(m):
    a,b= map(int,input().split())
    li.append((a,b))

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if(i < j or j < k):
                continue
            if(i == j or j == k or i == k):
                continue
            
            check = [i,j,k]
            for a in range(len(li)):
                cnt = 0

                for b in range(3):
                    if(check[b] in li):
                        cnt += 1
                
                if(cnt >= 2):
                    continue

print(ans)