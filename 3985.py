import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
ans1 = 0
ans1_val = 0

li = [0] * (n+1)

for i in range(1, k+1): 
    s, e = map(int, input().split())
    if(e-s > ans1_val):
        ans1_val = e-s
        ans1 = i

    for j in range(s, e+1):
        if(li[j] == 0):
            li[j] = i
    
check = [0] * (k+1)
for i in range(len(li)):
    check[li[i]] += 1

ans2 = 0
ans2_val = 0
for i in range(1, k+1):
    if(check[i] > ans2_val):
        ans2_val = check[i]
        ans2 = i

print(ans1)
print(ans2)
