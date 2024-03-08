P, K = map(int, input().split())
res = True
for i in range(2, K):
    if P % i == 0:
        res = False
        break
if res:
    print("GOOD")
else:
    print(f"BAD {i}")