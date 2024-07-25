import sys
input = sys.stdin.readline

li = []
for _ in range(5):
    k = int(input())
    li.append(k)

if(li[0] < 0):
    print((abs(li[0]) * li[2]) + li[3] + (li[1] * li[4]))
else:
    print((li[1] - li[0]) * li[4])