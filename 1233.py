s1,s2,s3=map(int,input().split())
ans = [0] * (101)

for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            ans[i+j+k] += 1
max_val = 0
ans_idx = 0
for i in range(101):
    if(ans[i] > max_val):
        ans_idx = i
        max_val = ans[i]
print(ans_idx)