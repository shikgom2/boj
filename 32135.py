import sys
input = sys.stdin.readline

n = int(input())
li = [1]

cur = 3
while(True):
    if(cur != 7):   
        li.append(cur)
    cur += 2
    if(cur > n):
        break
li.append(7)
li.append(2)
cur = 4
while(True):
    if(cur != 8):   
        li.append(cur)
    cur += 2
    if(cur > n):
        break

li.append(8)

for i in range(n):
    for j in range(n):
        print(li[(i+j) % n], end=" ")
    print()