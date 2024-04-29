ans = 0
a,b = map(str, input().split())

for i in range(len(a)):
    for j in range(len(b)):
        ans += int(a[i]) * int(b[j])

print(ans)