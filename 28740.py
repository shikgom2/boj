import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = []

for i in range(n):
    t1, t2 = map(int, input().split('.'))
    k.append(t1 * 10 + t2)

res = 0
for i in range(n):
    res += max(
        a[i] * k[i] // 10 - b[i], 
        a[i] - b[i] * k[i] // 10
    )

print(res)