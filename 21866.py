arr = [100, 100, 200, 200, 300, 300, 400, 400, 500]
li = list(map(int, input().split()))
s, ans = 0, 0

for i in range(9):
    if(li[i] > arr[i]):
        ans = 1
    s += li[i]

if ans:
    print("hacker")
else:
    print("draw" if s >= 100 else "none")