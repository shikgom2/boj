import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    if(k%9==0):
        print("YES")
    else:
        print("NO")