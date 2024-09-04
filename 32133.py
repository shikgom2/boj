import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
li = []

#input
for _ in range(n):
    s = list(map(str, input().rstrip()))
    li.append(s)

#check find
flag = False
ans = ""
for i in range(1, m+1): #substring Index
    dic = dict() #count dictonary
    for j in range(n):
        ss = str(li[j][:i]) #substring from 1~i
        if(ss not in dic): #update count
            dic[ss] = 1
        else:
            dic[ss] += 1

    for key, value in dic.items(): 
        if(value <= k): #survives under k
            ans = key
            flag = True
            break
    if(flag):
        break

res = []
for i in range(len(ans)):
    if(ans[i].isalpha()):
        res.append(ans[i])

if(len(res) == 0):
    print(-1)
else:
    #print how many survive
    print(len(res))
    #must print my victory way
    for i in range(len(res)):
        if(res[i] == 'S'):
            print("P",end="")
        elif(res[i] == 'R'):
            print("S",end="")
        elif(res[i] == 'P'):
            print("R",end="")