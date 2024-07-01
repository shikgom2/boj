import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li.sort(reverse=True)
ans = 0

while(True):

    if(len(li) == 1):
        break
    
    ans += (li[0] + li[1])
    del(li[1])

print(ans)