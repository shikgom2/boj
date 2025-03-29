import sys
input = sys.stdin.readline
import math

x1,y1,z1, x2,y2,z2 = map(int, input().split())
N = int(input())
li = list(map(int, input().split()))

S = sum(li)
max_l = max(li)

dx = x2 - x1
dy = y2 - y1
dz = z2 - z1
D = math.sqrt(dx*dx + dy*dy + dz*dz)

min_reach = max(0, 2*max_l - S)
max_reach = S

print("YES" if min_reach - 1e-9 <= D <= max_reach + 1e-9 else "NO")