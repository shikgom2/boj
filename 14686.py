import sys
input = sys.stdin.readline
n = int(input())

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

ans = 0
t1 = 0
t2 = 0
for i in range(n):
    t1 += li1[i]
    t2 += li2[i]
    if(t1 == t2):
        ans = (i+1)
print(ans)