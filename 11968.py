import sys
input = sys.stdin.readline

n = int(input())
li1 = []
for _ in range(n):
    a = int(input())
    li1.append(a)

li2 = [] # for me
for i in range(1, n*2 + 1):
    if(i not in li1):
        li2.append(i)

li1.sort()
li2.sort()
ans = 0
for i in range(len(li1)):
    for j in range(len(li2)):
        if(li1[i] < li2[j]):
            ans += 1
            li2[j] = 0
            break

print(ans)