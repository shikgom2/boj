import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
li = []
for _ in range(N):
    li.append(input().strip())
K = int(input())

dic = {}
for row in li:
    zero_count = row.count('0')
    if row in dic:
        dic[row][0] += 1
    else:
        dic[row] = [1, zero_count]

ans = 0
for pattern, (count, zero_count) in dic.items():
    if zero_count <= K and (K - zero_count) % 2 == 0:
        ans = max(ans, count)

print(ans)
