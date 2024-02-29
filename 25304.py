N = int(input())
k = int(input())
sum = 0
for _ in range(k):
    a,b = map(int, input().split())
    sum += (a*b)

if(sum == N):
    print("Yes")
else:
    print("No")