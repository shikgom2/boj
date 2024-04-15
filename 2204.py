while(True):
    n=int(input())
    if(n==0):
        break
    li = []
    for _ in range(n):
        i = input()
        li.append((i, i.lower()))
        
    li.sort(key=lambda k: k[1])
    print(li[0][0])