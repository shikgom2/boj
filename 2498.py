import sys
input = sys.stdin.readline

s1 = list(map(str, input().rstrip()))
s2 = list(map(str, input().rstrip()))
s3 = list(map(str, input().rstrip()))

ans = []
cnt = [0] * 4
check = []

checka = []
checkb = []
checkc = []

for i in range(len(s1)):
    #case 1 : all same
    if(s1[i] == s2[i] and s1[i] == s3[i] and s2[i] == s3[i]):
        ans.append(s1[i])
        
    #case 2 : only s1 different
    elif(s2[i] == s3[i]):
        ans.append(s2[i])
        cnt[1] += 1
        checka.append(i)

    #case 3 : only s2 different
    elif(s1[i] == s3[i]):
        ans.append(s1[i])
        cnt[2] += 1
        checkb.append(i)

    #case 4 : only s3 different
    elif(s1[i] == s2[i]):
        ans.append(s1[i])
        cnt[3] += 1
        checkc.append(i)

    #case 5 : all different
    else:
        ans.append(s1[i])
        check.append(i)

#check all different
while(len(check)):
    idx = check[0]
    del check[0]

    max_val = 0
    max_idx = 0
    #get maximum value
    for i in range(1, 4):
        if(max_val < cnt[i]):
            max_val = cnt[i]
            max_idx = i
    
    #update distance without max
    for i in range(1, 4):
        if(i != max_idx):
            cnt[i] += 1

    if(max_idx == 1):
        ans[idx] = s1[idx]
    elif(max_idx == 2):
        ans[idx] = s2[idx]
    elif(max_idx == 3):
        ans[idx] = s3[idx]

#check again

#0,0,+1 -> +1,+1,0 

while(True):
    max_val = max(cnt[1:4])
    max_idx = cnt.index(max_val)
    
    min_val = min(cnt[1:4])
    min_idx = cnt.index(min_val)
    if(max_val - min_val <= 1):
        break

    #change s1 -> s2,s3
    if(max_idx == 1):
        if(len(checka) == 0):
            break
        idx = checka[0]
        del checka[0]
        ans[idx] = s1[idx]

        cnt[1] -= 1
        cnt[2] += 1
        cnt[3] += 1

    #change s2 -> s1, s3
    elif(max_idx == 2):
        if(len(checkb) == 0):
            break    
        idx = checkb[0]
        del checkb[0]
        ans[idx] = s2[idx]

        cnt[1] += 1
        cnt[2] -= 1
        cnt[3] += 1
    
    #change s3 -> s1, s2
    elif(max_idx == 3):
        if(len(checkc) == 0):
            break
        idx = checkc[0]
        del checkc[0]
        ans[idx] = s3[idx]

        cnt[1] += 1
        cnt[2] += 1
        cnt[3] -= 1

print(max(cnt))
print(*ans, sep='')