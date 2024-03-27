N,W,H = map(int, input().split())
size = W*W + H*H

for _ in range(N):
    n = int(input())
    if(n*n <= size):
        print("DA")
    else:
        print("NE")