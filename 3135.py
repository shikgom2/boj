a,b = map(int, input().split())
k=int(input())
li = []
for _ in range(k):
    i = int(input())
    li.append(i)

ans = abs(a-b)
for i in li:
    ans = min(ans, abs(i-b)+1)

print(abs(ans))