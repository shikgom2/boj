n = int(input())
cnt = 0
for _ in range(n):
    k = input()
    k = k[2:]
    k = int(k)

    if(k <= 90):
        cnt += 1
print(cnt)