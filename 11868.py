n = int(input())
li = list(map(int, input().split()))
res = 0
for i in li:
    res = res ^ i
if(res==0):
    print("cubelover")
else:
    print("koosaga")