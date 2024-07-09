li = []
for _ in range(6):
    k = int(input())
    li.append(k)

ans = li[0] * 3 + li[1] * 2 + li[2]
ans2 = li[3] * 3 + li[4] * 2 + li[5]

if(ans>ans2):
    print("A")
elif(ans<ans2):
    print("B")
else:
    print("T")