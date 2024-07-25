n=int(input())
li=list(map(int, input().split()))
print(min(n, li[0]) + min(n, li[1]) + min(n, li[2]))
