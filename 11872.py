n=int(input())
li = list(map(int, input().split()))
ans = 0
for i in li:
    if(i%4 == 3):
        i += 1
    elif(i > 0 and i%4 == 0):
        i -= 1
    ans = ans ^ i

if(ans == 0):
    print("cubelover")
else:
    print("koosaga")