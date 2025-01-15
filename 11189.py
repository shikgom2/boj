t=int(input())
for i in range(t):
    d, n, s, p = map(int, input().split())
    
    s = n * s
    p = d + (n * p)
    
    if s < p:
        print("do not parallelize")
    elif s > p:
        print("parallelize")
    else:
        print("does not matter")
