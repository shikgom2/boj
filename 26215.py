import sys
input = sys.stdin.readline
import heapq as hq

n = int(input())
li = list(map(int,input().split()))
li = [-x for x in li]

hq.heapify(li)
ans = 0

while(True):
    ans += 1

    if(len(li) == 1):
        val = hq.heappop(li)
        val += 1
        if(val != 0):
            hq.heappush(li, val)
    else:
        val1 = hq.heappop(li)
        val1 +=1
        val2 = hq.heappop(li)
        val2 += 1
        if(val1 != 0):
            hq.heappush(li, val1)
        if(val2 != 0):
            hq.heappush(li, val2)

    if(len(li) == 0):
        if(ans > 1440):
            print(-1)
        else:
            print(ans)
        break