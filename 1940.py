import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
li = list(map(int, input().split()))

ans = 0
for i in range(len(li)):
    for j in range(len(li)):
        if(i == j):
            continue
        if(li[i] + li[j] == m):
            ans += 1
print(ans//2)