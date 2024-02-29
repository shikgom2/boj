from collections import deque

d = deque()
tmp = []

N = int(input())
for _ in range(N):
    s = input()
    i = s[0]
    if(len(s) > 1):
        j = s[2]

    print(j)
    flag = 0

    if(i==1):
        d.append(j)
        tmp.append(1) 
    elif(i==2):
        d.appendleft(j)
        flag = 2
        tmp.append(2)
    elif(i==3):
        if(tmp[len(tmp)-1] == 1):
            d.pop()
            tmp.pop()
        elif(tmp[len(tmp)-1] == 2):
            d.popleft()
            tmp.pop()
    print(d)

#print("".join(d))
print(d)