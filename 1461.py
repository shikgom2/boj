import sys
input = sys.stdin.readline

n,m = map(int, input().split())
li = list(map(int, input().split()))

plus = []
minus = []
for i in li:
    if(i >= 0):
        plus.append(i)
    else:
        minus.append(i)

plus.sort()
minus.sort()

print(plus)
print(minus)

ans = 0