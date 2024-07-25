n ,m = map(int, input().split())
a = 100 - n
b = 100 - m
c = 100 - (a + b)
d = a * b

ans = c * 100 + d
q = ans // 100 - c
r = d % 100

print(a, b, c, d, q, r)
print(ans // 100, ans % 100)