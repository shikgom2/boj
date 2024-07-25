a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())
ans1 = 0
ans2 = 0

if t <= 30:
    ans1 = a
else:
    ans1 = (a + (t - 30) * x) * 21 - a * 20
if t <= 45:
    ans2 = b
else:
    ans2 = (b + (t - 45) * y) * 21 - b * 20

print(ans1, ans2)