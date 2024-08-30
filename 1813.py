import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
ct = [0] * 51
for n in li:
    ct[n] += 1

for i in range(50, -1, -1):
    if ct[i] == i:
        print(i)
        break
else:
    print(-1)