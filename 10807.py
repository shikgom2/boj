n = int(input())
li = map(int, input().split())
k = int(input())
cnt=0

for i in li:
    if(i == k):
        cnt += 1
print(cnt)