n = int(input())
li = list(map(int, input().split()))
t, p = map (int, input().split())

print(sum(map(lambda x:(x+t-1)//t,li)))
print(*divmod(n,p))