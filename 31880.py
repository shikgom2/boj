n,m = map(int, input().split())
li = list(map(int, input().split()))
li2 = list(map(int, input().split()))

ans = sum(li)

for i in range(len(li2)):
    if(li2[i] != 0):
        ans *= li2[i]

print(ans)