N = int(input())
cnt = 0
for i in range(N):
    while i > 0:
        i, left = divmod(i, 10)
        if(left == 3 or left == 6 or left == 9):
            cnt += 1
print(cnt)