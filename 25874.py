def numdiv(n,div):
    res = 0
    while n%div == 0:
        res += 1
        n //= div
    return res

n = int(input())
twos = numdiv(n,2)
fives = numdiv(n,5)

base = 1
vals = []

for i in range(twos+1):

    cur = base
    for j in range(fives+1):
        vals.append(cur)
        cur *= 5

    base *= 2

vals.sort()

print(len(vals))
for i in range(len(vals)):
    print(vals[i])