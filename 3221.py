import sys
input = sys.stdin.readline

l, t = map(int, input().split())
n = int(input())
ans = []

for _ in range(n):
    pos, dir = input().split()
    pos = int(pos)

    if dir == "L": #left
        pos -= t
    else: #right
        pos += t

    pos = pos % (2 * l) #get even distance

    if pos > l: #get odd distance
        pos = 2 * l - pos

    ans.append(pos)

ans.sort()
print(' '.join(map(str, ans)))



