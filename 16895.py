n = int(input())
li = list(map(int, input().split()))
ans = 0
for i in range(len(li)):
    res = 0
    for j in range(len(li)):
        if(i == j):
            continue
        res = res ^ li[j]
    
    for j in range(li[i]):
        if((res ^ j) == 0):
            ans += 1
print(ans)