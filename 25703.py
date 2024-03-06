n = int(input())
print("int a;")

for i in range(1, n+1):
    print("int ",end="")
    for j in range(0, i):
        print("*",end="")
    if(i == 1):
        print(f"ptr = &a;", end="")
    elif(i == 2):
        print(f"ptr{i} = &ptr;", end="")
    else:          
        print(f"ptr{i} = &ptr{i-1};", end="")
    print()