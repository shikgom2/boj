import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [input().rstrip() for _ in range(n)]
li = []
for col in zip(*s):
    s = ''.join(col)
    li.append(int(s, 2))
    
s = set(li)
s = list(s)

p0 = s[0]
c = [p0]
for i in range(n):
    c.append(p0 ^ (1 << i))
cnt = 0
for y in c:
    flag = True
    for p in s:
        d = (y ^ p).bit_count()
        if d > 1:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)
