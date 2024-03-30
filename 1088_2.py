import sys
from decimal import Decimal
input = sys.stdin.readline

n = int(input())
tmp = list(map(int, input().split()))
k = int(input())

#Input
li = []
for i in tmp:
    #Input을 받을 때, (현재 값, 잘린 홧수) tuple 형식으로 받음
    #Decimal 실수 오차
    li.append((Decimal(i), Decimal(1)))

li.sort(key = lambda k: k[0], reverse = True)
#max - min
res = li[0][0] - li[len(li)-1][0]

for _ in range(k+1):
    li.sort(key = lambda k: k[0], reverse = True)
    #max - min
    res = min(res, li[0][0] - li[len(li)-1][0])

    #biggest value
    val = li[0][0]
    cnt = li[0][1]
    #기존 잘린 횟수 만큼 곱해 원래조각 크기를 구하고, 다시 +1 조각만큼 나눔.
    val = val * cnt / (cnt+1)

    #update biggest value
    li[0] = (val, cnt+1)
    
print(f"{res:.30f}")
