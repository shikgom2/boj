n = int(input())
r = list(map(int, input().split()))
li = []

l = list(map(int, input().split()))
for i in range(len(l)):
    li.append((l[i], i))

r_sum = sum(r)
c_sum = sum(x[0] for x in li)

if r_sum != c_sum:
    print(-1)
    exit()

ans = [[0] * n for _ in range(n)]

for i in range(n):
    check = r[i]
    li.sort(reverse=True, key=lambda x: x[0])
    for j in range(n):
        if check == 0:
            break
        if li[j][0] > 0:
            check -= 1
            li[j] = (li[j][0] - 1, li[j][1])
            ans[i][li[j][1]] = 1
    
    if check > 0:
        print(-1)
        exit()

print(1)
for r in ans:
    print(''.join(map(str, r)))