import sys
input = sys.stdin.readline

n = int(input())
li = list(map(str, input().rstrip()))
for i in range(n-1):
    if(li[i+1] == 'J'):
        print(li[i])