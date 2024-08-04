import sys
input = sys.stdin.readline

n = int(input())
li = list(map(str, input().rstrip()))

#1. red front
ans1 = 0
flag = True
for i in range(len(li)):
    if(flag and li[i] == 'B'):
        flag = False
    if(flag == False and li[i] == 'R'):
        ans1 += 1

#2. blue front
ans2 = 0
flag = True
for i in range(len(li)):
    if(flag and li[i] == 'R'):
        flag = False
    if(flag == False and li[i] == 'B'):
        ans2 += 1

#3. red back
li2 = li.copy()
li2.reverse()
ans3 = 0
flag = True
for i in range(len(li2)):
    if(flag and li2[i] == 'B'):
        flag = False
    if(flag == False and li2[i] == 'R'):
        ans3 += 1

#4. red back
li2 = li.copy()
li2.reverse()
ans4 = 0
flag = True
for i in range(len(li2)):
    if(flag and li2[i] == 'R'):
        flag = False
    if(flag == False and li2[i] == 'B'):
        ans4 += 1

print(min(ans1, ans2, ans3, ans4))