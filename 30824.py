import sys
input = sys.stdin.readline 

#bruteforce.
t = int(input())

fibo = [0] * 90
#i th sum
fibo[1] = 1
fibo[2] = 1

for i in range(3, 90):
    fibo[i] = fibo[i-1] + fibo[i-2]
li = []
for i in range(1, 90):
    li.append(fibo[i])


#200*200*200 each query * 100 TLE.
for _ in range(t):
    k, x = map(int, input().split())
    flag = False
    if(k == 1):
        for i in range(len(li)):
            if(li[i] == x):
                flag = True
                break
    elif(k == 2):
        for i in range(len(li)):
            for j in range(len(li)):
                if(li[i] + li[j] == x):
                    flag = True
                    break
    elif(k == 3):
        for i in range(len(li)):
            for j in range(len(li)):
                for k in range(len(li)):
                    if(li[i] + li[j] + li[k] == x):
                        flag = True
                        break 
    if(flag):
        print("YES")
    else:
        print("NO")