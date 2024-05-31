N, S, R = map(int, input().split())

b = set(map(int, input().split()))
o = set(map(int, input().split()))

ans = 0

i = b & o
b = list(b - i)
o = list(o - i)

b.sort()

for t in b:
    if t-1 in o:
        o.remove(t-1)
    elif t+1 in o:
        o.remove(t+1)
    else:
        ans += 1  

print(ans)