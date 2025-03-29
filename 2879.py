import sys
input = sys.stdin.readline

n = int(input())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

diff = [li2[i] - li1[i] for i in range(n)]
ans = abs(diff[0])

for i in range(1, n):
    ans += abs(diff[i] - diff[i-1])
ans += abs(diff[-1])

print(ans // 2)