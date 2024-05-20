import sys
input = sys.stdin.readline

n = int(input())
li = [0] * 50001

arr = list(map(int, input().split()))
for i in range(n):
    k = arr[i]
    
    if(li[k] == 1):
        print(k+1, end=" ")
    elif(k > 1 and not li[k - 1]):
        print(k-1, end=" ")
        li[k-1] = 1
        li[k] = 2
    else:
        print(k, end=" ")
        li[k] = 1