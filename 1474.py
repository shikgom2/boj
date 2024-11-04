import sys
input = sys.stdin.readline 

li = []

n, k = map(int, input().split())
lens = 0

for _ in range(n):
    s = input().rstrip()
    li.append(s)
    lens += len(s)

freq = (k-lens) // (n-1)
over = (k-lens) - (freq * (n-1))


print(li[0],end="")

for i in range(1, len(li)):
    if(ord(li[i][0]) >= 97 and over > 0):
        print('_' * (freq+1), end="")
        over -= 1
    elif(len(li) - i - over == 0):
        print('_' * (freq+1), end="")
        over -= 1
    else:
        print("_" * freq, end="")
    
    print(li[i], end="")