li=list(map(int,input().split()))
li.sort()
print(abs((li[0]+li[3]) - (li[1] + li[2])))