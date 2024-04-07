import sys
input = sys.stdin.readline

l, t = map(int,input().split())
n = int(input())
ant = []
ans = []

for _ in range(n):
    a, b = input().split()
    ant.append([int(a), b])

for i in ant:
    if i[1] == "L": #Left
        dist = t + l - i[0]
        if dist < l:
            ans.append(l-dist)
        else:
            if (dist//l) % 2 == 1:
                ans.append(dist%l)
            else:
                ans.append(l - dist%l)

    else: #Right
        dist = t + i[0]
        if dist < l:
            ans.append(dist)
        else:
            if (dist // l) % 2 == 1:
                ans.append(l - dist%l)
            else:
                ans.append(dist % l)
ans.sort()
print(' '.join(map(str,ans)))