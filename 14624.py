import sys
input = sys.stdin.readline

n = int(input())
if not(n%2):
    print("I LOVE CBNU")
else:
    graph = [[" "] * n for _ in range(n)]
    print("*" * n)
    print(" " * (n//2),end="")
    print("*", end="")
    print(" " * (n//2))
    
    s = n//2-1
    e = n//2 + 1
    
    for i in range(n//2):
        graph[i][s] = "*"
        graph[i][e] = "*"
        
        print(" " * s, end="")
        print("*", end="")
        print(" " * (e-s-1), end="")
        print("*")
        
        s -= 1
        e += 1