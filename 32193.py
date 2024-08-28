import sys
input = sys.stdin.readline

n = int(input())
cura = 0
curb = 0
for _ in range(n):
    a,b = map(int, input().split())
    cura += a
    curb += b
    print(cura - curb)