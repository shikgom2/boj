import sys
input = sys.stdin.readline

n = list(map(str,input().rstrip()))

i = 1
cur = 0
while cur <len(n) :
    temp = str(i)

    for j in range(len(temp)):
        if cur >= len(n):
            break
        if temp[j] == n[cur]:
            cur+=1
    i+=1

print(i-1)
