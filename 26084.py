import sys
input = sys.stdin.readline 

init = list(map(str, input().rstrip()))
n = int(input())
li = []

cnt = [0] * 26
for _ in range(n):
    s = list(map(str, input().rstrip()))
    cnt[ord(s[0])-65] += 1

if(init[0] == init[1] and init[0] and init[2]):
    print(n - 1)
    
print(cnt)