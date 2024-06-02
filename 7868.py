import sys
input = sys.stdin.readline

p1, p2, p3, x = map(int, input().split())
li = []
INF = 10**18

for i in range(60):
    pow1 = p1**i
    if pow1 > INF:
        break
    for j in range(60):
        pow2 = pow1 * p2**j
        if pow2 > INF:
            break
        for k in range(60):
            if i + j + k == 0:
                continue
            pow3 = pow2 * p3**k
            if pow3 > INF:
                break
            li.append(pow3)

li.sort()
print(li[x-1])