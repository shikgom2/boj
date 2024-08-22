import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    li = []
    
    max_width = 0
    max_height = 0
    for _ in range(n):
        a,b,c,d = map(int, input().split())
        li.append((a,b,c,d))
        
    for i in range(len(n)):
        