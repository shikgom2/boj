import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    li = list(map(str,input().rstrip()))
    print(int(li[0]) + int(li[2]))