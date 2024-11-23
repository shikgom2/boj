import sys
input = sys.stdin.readline

li = list(map(int, input().split()))

ans1 = sum(li) / 20

target = -1
for i in range(len(li)):
    if(li[i] == 20):
        target = i

ans2 = 0
if(target == 0):
    ans2 = li[0] + li[1] + li[19]
elif(target == 19):
    ans2 = li[18] + li[19] + li[0]
else:
    ans2 = li[target-1] + li[target] + li[target+1]

ans2 /= 3


if(ans1 == ans2):
    print("Tie")
elif(ans1 > ans2):
    print("Bob")
else:
    print("Alice")