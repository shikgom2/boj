import sys
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
    n = int(input())
    i = 0
    while(n):
        if(n%2):
            print(i, end=" ")
        n //= 2
        i += 1
    print()