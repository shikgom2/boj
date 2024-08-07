import sys
input = sys.stdin.readline 

n,h,w = map(int, input().split())
li = []

for _ in range(h):
    s = list(map(str, input().rstrip()))
    li.append(s)

#n^3
ans = []
for i in range(0, n*w, w):
    tmp = "?"
    for j in range(0, h): #sero
        for k in range(i, i+w): #garo
            if('?' != li[j][k]):
                tmp = li[j][k]
    ans.append(tmp)
print(*ans, sep="")