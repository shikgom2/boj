n = int(input())
li = list(map(int, input().split()))
res = 0
flag = 0
for i in li:
    res = res ^ i
    flag = flag | (res > 1)

if flag:
    print("cubelover" if not res else "koosaga")
else:
    print("cubelover" if res else "koosaga")