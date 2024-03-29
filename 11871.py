n = int(input())
res = 0

li = list(map(int, input().split()))
for i in li: 

    if(i % 2 == 0):
        res = res ^ (i-2) // 2
    else:
        res = res ^ (i+1) // 2

if(res > 0):
    print("koosaga")
else:
    print("cubelover")