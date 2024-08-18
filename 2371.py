import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    l = list(map(int, input().split()))
    li.append(l[:-1])

for i in range(1, 10**10):
    s = set()
    for j in range(n):
        s.add(tuple(li[j][:i]))
    
    if(len(s) == n):
        print(i)
        break