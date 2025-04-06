import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [input().strip() for _ in range(n)]
li2 = [input().strip() for _ in range(n)]

flag = True
for i in range(n):
    tmp = ''.join(c * 2 for c in li[i])
    if tmp != li2[i]:
        flag = False
        break

print("Eyfa" if flag else "Not Eyfa")
