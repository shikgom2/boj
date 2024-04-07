n=int(input())
for _ in range(n):
    i,j = map(int, input().split())
    
    if(j%2 == 1):
        if(i%2 == 1):
            print("1")
        else:
            print("0")
    else:
        i = i % (j+1)
        if(i == j):
            print(j)
        elif(i%2 == 1):
            print(1)
        else:
            print(0)