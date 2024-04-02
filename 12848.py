n,m = map(int, input().split())
grundy = []
for _ in range(n):
    li = list(map(str, input().strip()))
    
    cnt = 0
    for i in range(len(li)):
        #print(i)
        if(li[i] == '@' and cnt >= 1):
            grundy.append(cnt)
            cnt = 0
        else:   
            cnt += 1
            if(i == len(li)-1):
                grundy.append(cnt)
                cnt = 0
    
i = int(input())
li = list(map(int, input().split()))

print(grundy)

ans = 0
for i in grundy:
    ans = ans ^ i
    
if(ans != 0):
    print("nein")
else:
    print("hyo123bin")