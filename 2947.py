n = int(input())
res = 0
for i in range(n):
    h, b, k = map(int, input().split())
    if b-h > 0:
        res += (b-h)*k
print(res)