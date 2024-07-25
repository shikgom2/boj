import sys
input = sys.stdin.readline

r,c,n= map(int, input().split())

if(r%n):
    row = r // n + 1
else:
    row = r//n
if(c%n):
    col = c // n + 1
else:
    col = c//n
ans = row*col
print(ans)