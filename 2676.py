import sys
input = sys.stdin.readline

N = int(input())
while(N):
    n,m = map(int, input().split())
    print((n-m) * m + 1)
    N-=1