import sys
input = sys.stdin.readline

n = int(input())
li = [0] * 50001

for i in range(n):
    k = int(input())
    
    if(li[k] == 1):
        print(k+1)
    elif(k > 1 and not li[k - 1]):
        print(k-1)
        li[k-1] = 1
        li[k] = 2
    else:
        print(k)
        li[k] = 1