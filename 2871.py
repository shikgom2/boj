from collections import deque

MAXN = 100100

n = int(input())
A = input().strip()

taken = [0] * n

ans = []
ans1 = []

li = [deque() for _ in range(26)]

for i in range(n - 1, -1, -1):
    li[ord(A[i]) - ord('a')].append(i)

m = n - 1
s = 0

for i in range(n):
    if(i % 2 == 1):
        while True:
            while not li[s]:
                s += 1
            if taken[li[s][0]]:
                li[s].popleft()
                continue
            break
        ans1.append(chr(ord('a') + s))
        taken[li[s].popleft()] = 1
    else:
        while taken[m]:
            m -= 1
        ans.append(A[m])
        taken[m] = 1

if(''.join(ans1) < ''.join(ans)):
    print("DA")
else:
    print("NE")

print(''.join(ans1))