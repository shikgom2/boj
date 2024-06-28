import sys
input = sys.stdin.readline
import itertools

n,f = map(int, input().split())

li = []
for i in range(1, n+1):
    li.append(i)
    
com = itertools.permutations(li, n)

for c in com:
    li = list(c) 
    tmp = li.copy()
    while(len(li) > 1):
        k = len(li)
        for i in range(0, k-1):
            li.append(li[i] + li[i+1])
        
        del(li[0:k])
        
    if(li[0] == f):
        print(*tmp)
        exit()