import sys
input = sys.stdin.readline

while(True):
    n = int(input())
    if not n:
        break

    li = []

    for _ in range(n):
        name, key = map(str, input().split())
        li.append((name, float(key)))
    
    li.sort(key=lambda x:x[1], reverse=True)

    m = 0
    ans = []
    for i in range(len(li)):
        if(m < li[i][1]):
            ans = []
            ans.append(li[i][0])
            m = li[i][1]
        elif(m == li[i][1]):
            ans.append(li[i][0])
        else:
            break

    print(*ans)