s = 0
m = 0
for _ in range(10):
    i,j = map(int, input().split())
    s = s + (j-i)
    m = max(m,s)
print(m)