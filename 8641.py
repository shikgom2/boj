import sys
input = sys.stdin.readline

n = int(input())
li = {}

for _ in range(n):
    a ,b = map(int, input().split())
    
    if(a not in li):
        li[a] = b
    else:
        li[a] += b

li = list(li.items())
print(len(li))

for i in range(len(li)):
    print(li[i][0], li[i][1])