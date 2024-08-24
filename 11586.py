import sys
input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    s = list(map(str, input().rstrip()))
    li.append(s)

k = int(input())

if(k == 1):
    for i in range(n):
        print(*li[i],sep="")
elif(k == 2):
    for i in range(n):
        li[i].reverse()
        print(*li[i], sep="")
elif(k == 3):
    for i in range(n-1, -1, -1):
        print(*li[i],sep="")