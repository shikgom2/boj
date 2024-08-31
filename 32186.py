import sys
input = sys.stdin.readline

n,k = map(int, input().split())
li = list(map(int, input().split()))

ans = 0

for i in range(n//2):
    cur1 = max(li[i], li[n-i-1])
    cur2 = min(li[i], li[n-i-1])

    diff = cur1 - cur2
    full = diff // k
    diff -= full * k
    ans += full
    ans += min(diff , k - diff + 1)

print(ans)