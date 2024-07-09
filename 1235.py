import sys
input = sys.stdin.readline

t = int(input())
li = []

for _ in range(t):
    s = list(map(str, input().rstrip()))
    s.reverse()
    li.append(s)

ans = 0
cur = 0
while(True):
    cur += 1
    li2 = [tuple(l[:cur]) for l in li]
    unique = set(li2)
    if(len(unique) == t):
        print(cur)
        exit()