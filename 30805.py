import sys
input = sys.stdin.readline

n = int(input())
t1 = list(map(int, input().split()))
li1 = []
for i in range(n):
    li1.append((t1[i], i))
    
m = int(input())
t2 = list(map(int, input().split()))
li2 = []
for i in range(n):
    li2.append((t2[i], i))

li1.sort(key=lambda x: (x[0], -x[1]), reverse=True)
li2.sort(key=lambda x: (x[0], -x[1]), reverse=True)

ans = []
idxa = 0
idxb = 0
limita = 0
limitb = 0

while idxa < n and idxb < m:
    if li1[idxa][0] == li2[idxb][0]:
        if limita > li1[idxa][1]:
            idxa += 1
        elif limitb > li2[idxb][1]:
            idxb += 1
        else:
            limita = li1[idxa][1]
            limitb = li2[idxb][1]
            ans.append(li1[idxa][0])
            idxa += 1
            idxb += 1
    elif li1[idxa][0] > li2[idxb][0]:
        idxa += 1
    else:
        idxb += 1

print(len(ans))
print(" ".join(map(str, ans)))