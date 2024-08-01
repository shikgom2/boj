n = int(input())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
ans = 0
for i in range(n):
    if li1[i] <= li2[i]:
        ans += 1
print(ans)