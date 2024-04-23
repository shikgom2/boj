n=int(input())
li=list(map(int,input().split()))
s=sum(li)+(8*(len(li)-1))
print(s//24, s%24)