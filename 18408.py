li = list(map(int, input().split()))
ans = 0
for i in li:
    if(i == 1):
        ans += 1
if(ans == 2 or ans == 3):
    print(1)
else:
    print(2)