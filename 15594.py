import sys
input = sys.stdin.readline

n = int(input())
li = []
li2 = []

for _ in range(n):
    k = int(input())
    li.append(k)
    li2.append(k)

li2.sort()
ans = 0
check = [0] * 1000001
for i in range(n):
    if(check[li[i]] == 0 and li[i] != li2[i]):
        check[li[i]] = 1
        ans += 1
if(ans == 0):
    print(0)
else:
    print(ans -1)