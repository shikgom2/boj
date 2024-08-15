import sys
input = sys.stdin.readline

n=int(input())
li = list(map(int, input().split()))

li.sort(reverse=True)

if(n==1):
    print(li[0])
elif(n==2):
    print(sum(li)-1)
else:
    a = 1
    if(n%3 == 0):
        b = n//3+1
    else:
        b = n//3+2

    if(n%3==2):
        c = b+(n//3)+1
    else:
        c = b+(n//3)
    #print(a,b,c)
    print(li[a-1] + li[b-1] + li[c-1] - 3)