import sys
input = sys.stdin.readline

li1 = [0] * 1001
li2 = [0] * 1001

for _ in range(3):
    a,b=  map(int, input().split())
    li1[a] += 1
    li2[b] += 1

for i in range(1001):
    if(li1[i] == 1):
        print(i,end=" ")

for i in range(1001):
    if(li2[i] == 1):
        print(i,end=" ")