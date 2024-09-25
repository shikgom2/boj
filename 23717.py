import sys
input = sys.stdin.readline
import copy

dic = {'R':['R'], 'B':['B'], 'Y':['Y'], 'O':['R', 'Y'], 'P':['R', 'B'], 'G':['Y', 'B'], 'A':['R', 'Y', 'B'], 'U':[]}
t = int(input())

for ttt in range(t):
    n = int(input())
    s = input().rstrip()
    li = []
    for i in range(n):
        li.append(copy.deepcopy(dic[s[i]]))
    cnt = 0
    
    li1 = [0] * n
    li2 = [0] * n
    li3 = [0] * n

    for i in range(len(li)):
        if 'R' in li[i]:
            li1[i] = 1
        if 'B' in li[i]:
            li2[i] = 1
        if 'Y' in li[i]:
            li3[i] = 1

    if li1[0] == 1:
        cnt += 1
    for i in range(1,n):
        if li1[i-1]==0 and li1[i]==1:
            cnt += 1
    if li2[0] == 1:
        cnt += 1
    for i in range(1,n):
        if li2[i-1]==0 and li2[i]==1:
            cnt += 1 
    if li3[0] == 1:
        cnt += 1
    for i in range(1,n):
        if li3[i-1]==0 and li3[i]==1:
            cnt += 1

    print(f'Case #{ttt+1}: '+ str(cnt))