n = int(input())
li = []
for _ in range(n):
    k=int(input())
    li.append(k)

ans = 10**10
for p in li:
    for q in li:
        sol = 0
        for x in li:
            sol += min((x - p) * (x - p), (x - q) * (x - q))
        ans = min(ans, sol)
print (ans)
