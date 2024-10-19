import sys
input = sys.stdin.readline 

n,m = map(int, input().split())
ans = 0
li = []

for _ in range(n):
    a,b = map(int, input().split())
    if(5 * a >= a * b): #can solve now
        ans += b
    else:
        li.append((a,b, m - (a*b)))
        
li.sort(key = lambda x : x[0], reverse=True)
#print(li)
cur = 0

#k * t - 5k

for i in range(len(li)):
    #cant solve now
    if(cur > li[i][2]):
        ans += (cur - li[i][2])
        cur = li[i][2]
        #print("update !", cur)
        
    ans += li[i][1] #update time
    cur = cur + ((li[i][0] * li[i][1]) - (5 * li[i][0])) #kt - 5k
    cur = max(0, cur)
    #print("curr rage : ", cur)

print(ans)