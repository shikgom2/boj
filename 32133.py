import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
li = []
for _ in range(n):
    s = list(map(str, input().rstrip()))
    li.append(s)

flag = False
ans = ""
for i in range(1, m+1):
    dic = dict()
    for j in range(n):
        ss = str(li[j][:i])
        if(ss not in dic):
            dic[ss] = 1
        else:
            dic[ss] += 1

    print(dic)
    for key, value in dic.items():
        if(value <= k):
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
    print(len(res))

    for i in range(len(res)):
        if(res[i] == 'S'):
            print("P",end="")
        elif(res[i] == 'R'):
            print("S",end="")
        elif(res[i] == 'P'):
            print("R",end="")