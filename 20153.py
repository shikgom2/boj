import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))

tmp = 0

for i in range(len(li)):
    tmp ^= li[i]

tmp2 = 0
for i in range(len(li)):
    tmp2 = max(tmp2, tmp ^ li[i])
    
print(max(tmp,tmp2), end="")
print(max(tmp,tmp2), end="")