d, p, q = map(int, input().split())
if p < q: 
    p, q = q, p

ans = 10*15
for i in range(min(q, d // p + 2)):
    res = (d - p * i) // q
    for j in range(max(0, res - 2), res + 3):
        if p * i + q * j < d:
            continue
        ans = min(ans, p * i + q * j)
print(ans)