import sys
input = sys.stdin.readline

n = int(input())
li = [0] * 21
for _ in range(n):
    query = input().rstrip()
    check = query.split(" ")
    if(len(check) == 2):
        idx = int(check[1])
    if(check[0] == 'add'):
        li[idx] = 1
    elif(check[0] == 'remove'):
        li[idx] = 0
    elif(check[0] == 'check'):
        if(li[idx]):
            print(1)
        else:
            print(0)
    elif(check[0] == "toggle"):
        if(li[idx]):
            li[idx] = 0
        else:
            li[idx] = 1
    elif(check[0] == 'all'):
        for i in range(1, 21):
            li[i] = 1
    elif(check[0] == 'empty'):
        for i in range(1, 21):
            li[i] = 0