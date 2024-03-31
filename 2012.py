n=int(input())
li = []
for _ in range(n):
    i = int(input())
    li.append(i)

li.sort()
ans = 0
cur = 0
for i in li:
    cur += 1
    ans += abs(cur - i) 
print(ans)