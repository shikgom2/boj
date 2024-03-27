while(True):
    li = list(map(int, input().split()))
    
    li.sort()
    if(li[0] == 0):
        break
    
    if(li[0] + li[1] <= li[2]):
        print("Invalid")
    elif(li[0] == li[1] and li[1] == li[2]):
        print("Equilateral")
    elif(li[0] == li[1] or li[1] == li[2]):
        print("Isosceles")
    else:
        print("Scalene")