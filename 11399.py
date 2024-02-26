n = int(input())
res = 0

li = list(map(int, input().split()))
li.sort()

for i in range(n):
    res += li[i] * (n-i)
print(res)