import sys
input = sys.stdin.readline

li = []
for _ in range(8):
    k = int(input())
    li.append(k)
tmp = li.copy()
li.sort(reverse=True)
print(sum(li[:5]))
ans = []
for i in range(5):
    ans.append(tmp.index(li[i])+1)
ans.sort()
print(*ans, sep=" ")