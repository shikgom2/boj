import sys
input = sys.stdin.readline

n = int(input())
li = list(map(str,input().rstrip()))
for i in range(n):
    if(li[i] == 'I'):
        li[i] = 'i'
    else:
        li[i] = 'L'
print(*li, sep="")