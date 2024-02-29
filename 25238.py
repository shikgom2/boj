n, m = map(int, input().split())
m = ((100 - m) * 0.01)
print(m)
res = n * m
if(res >= 100):
    print(1)
else:
    print(0)