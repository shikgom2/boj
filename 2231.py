a =input()
b = 9 * (len(a))
k = int(a)
for i in range(k-b,k):
    c = str(i)
    d = i
    for e in c:
        if e == '-':
            pass
        else:
            d += int(e)
    if d == int(a):
        print(i)
        break
else:
    print(0)