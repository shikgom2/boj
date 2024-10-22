import sys
input = sys.stdin.readline

n,t,c,p = map(int, input().split())

print((n-1)//t*c*p)