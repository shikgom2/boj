li = list(map(int,list(input())))
ans = 0
for i in range(len(li)):
    for j in range(i+1, len(li),2):
        sub = li[i:j+1]
        if sum(sub[:len(sub)//2]) == sum(sub[len(sub)//2:]):
            if ans < len(sub):
                ans = len(sub)
print(ans)