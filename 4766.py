import sys
input = sys.stdin.readline

cur = float(input())

while(True):
    n = float(input())
    if(n == 999):
        break
    ans = n - cur
    print(f"{ans:.2f}") 
    cur = n