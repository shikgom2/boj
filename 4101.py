while(True):
    i,j = map(int, input().split())
    if(i==0 and j==0):
        break
    if(i>j):
        print("Yes")
    else:
        print("No")
