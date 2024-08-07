import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

cnt = [0] * (n+1)
for i in range(len(li)):
    cnt[li[i]] += 1
mn = 0
ans = 0
flag = False
for i in range(1, n+1):
    if(mn < cnt[i]):
        ans = i
        mn = cnt[i]
        flag = False
    elif(mn == cnt[i]):
        flag = True

if(flag):
    print("skipped")
else:
    print(ans)