import sys
input = sys.stdin.readline
import math

n,m = map(int, input().split())

is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False
sqrt_n = int(math.isqrt(n)) +1
for p in range(2, sqrt_n):
    if is_prime[p]:
        for multiple in range(p*p, n+1, p):
            is_prime[multiple] = False

prefix = [0] * (n+1)
count =0
for i in range(1, n+1):
    if is_prime[i]:
        count +=1
    prefix[i] = count

for _ in range(m):
    a,b = map(int, input().split())
    if a > b or a <1 or b >n:
        print(0)
        continue

    cnt = prefix[b] - prefix[a-1]
    if a <=1 and b >=1:
        cnt +=1
    print(cnt)