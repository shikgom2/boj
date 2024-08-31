import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    s = input().rstrip()
    if(s not in dic):
        dic[s] = 1
    else:
        dic[s] += 1

ans = ""
max = 0
for idx, val in dic.items():
    if(val > max):
        ans = idx
        max = val
    
    if(val == max and ans > idx):
        ans = idx
print(ans)