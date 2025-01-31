n = int(input())
li = list(map(int, input().split()))

ans = 0
for i in range(len(li)):
    if(li[i]%2 == 1):
        li[i] += 1

    if(li[i] == 1 or li[i] == 2):
        ans += 1
    else:
        ans += (li[i]//2)
    
print(ans)