import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
li = []

for i in range(n):
    s = list(map(int, input().split()))
    li.append(s)

ans1, ans2 = 0, 10**10

for i in range(257):
    time = 0
    blocks = b

    for j in range(n):
        for k in range(m):
            if(li[j][k] > i): #dig
                time += abs(li[j][k] - i) * 2
                blocks += abs(li[j][k] - i)
            elif(li[j][k] < i): #set
                time += abs(li[j][k] - i)
                blocks -= abs(li[j][k] - i)

    if(blocks >= 0):
        if(time <= ans2):
            ans1 = i
            ans2 = time

print(ans2, ans1)