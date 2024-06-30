import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
li = []

for _ in range(n):
    x, y = map(int, input().split())
    li.append((x,y))
li.sort()

st = []
ans = 0
for _, val in li:
    while st and st[-1] > val:
        st.pop()
    if val and (not st or st[-1] < val):
        st.append(val)
        ans += 1

print(ans)