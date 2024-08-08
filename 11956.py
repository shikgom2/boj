import sys
input = sys.stdin.readline
MAXN = 100010

n = int(input())
li = list(map(int, input().split()))
pref_xor = [0] * (2 * MAXN)

for i in range(1, n+ 1):
    pref_xor[i] = pref_xor[i - 1] ^ li[i - 1]

for i in range(n + 1):
    pref_xor[i + n + 1] = pref_xor[i]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    r = l % (n + 1) + (r - l + 1) % (n + 1)
    l %= n + 1
    print(pref_xor[r] ^ pref_xor[l])