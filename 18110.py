import sys
input = sys.stdin.readline

n = int(input())
if(n == 0):
    print(0)
    exit()
    
li = []
for _ in range(n):
    a = int(input())
    li.append(a)

t = int(n * 3 / 20 + 0.5)
ans = int(sum(sorted(li)[t:n - t]) / (n - t * 2) + 0.5)
print(ans)