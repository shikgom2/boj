n = int(input())
li = sorted(list(map(int, input().split())), reverse = True)
ans = 0

for i, j in enumerate(li):
    ans = max(ans, i+j+2)
print(ans)