import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

ans = 0
for i in range(len(li)):
    if(li[i] % 8 == 7):
        ans = ans ^ (li[i]+1)
    elif(li[i] % 8 == 0):
        ans = ans ^ (li[i]-1)
    else:
        ans = ans ^ li[i]

if(ans):
    print("First")
else:
    print("Second")