k = int(input())
ans = k / 100 + 25
if ans > 2000:
    ans = 2000
if ans < 100:
    ans = 100
print("{:.2f}".format(ans))