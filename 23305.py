import sys
input = sys.stdin.readline

n = int(input())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

dic = {}
for i in range(len(li1)):
    if(li1[i] not in dic):
        dic[li1[i]] = 1
    else:
        dic[li1[i]] += 1

ans = 0
for i in range(len(li2)):
    if(li2[i] in dic and dic[li2[i]] > 0):
        ans += 1
        dic[li2[i]] -= 1 

print(n - ans)