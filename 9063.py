n =  int(input())
x = []
y = []
if n == 1:
    print(0)
else:
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    res = (max(x) - min(x)) * (max(y) - min(y))
    print(res)