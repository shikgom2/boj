import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
t2 = list(map(int, input().split()))

t.sort()
t2.sort()

li = []
li2 = []

for i in range(len(t)):
    li.append([t[i], False])
for i in range(len(t2)):
    li2.append([t2[i], False])  

li.sort()
li2.sort(reverse=True)

ans = 0
for i in range(n):
    for j in range(n):
        if(li[i][1] == False and li2[j][1] == False and li[i][0] > li2[j][0]):
            ans += 2
            li[i][1] = True
            li2[j][1] = True
            break

for i in range(n):
    for j in range(n):
        if(li[i][1] == False and li2[j][1] == False and li[i][0] == li2[j][0]):
            ans += 1
            li[i][1] = True
            li2[j][1] = True
            break

for i in range(n):
    for j in range(n):
        if(li[i][1] == False and li2[j][1] == False and li[i][0] < li2[j][0]):
            #ans -= 50
            li[i][1] = True
            li2[j][1] = True
            break
print(ans)
