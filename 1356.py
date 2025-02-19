
N = input().strip() 
if len(N) == 1:
    print("NO")
    exit()

for i in range(1, len(N)):
    front_part = N[:i]
    back_part = N[i:]
    
    front_product = 1
    for digit in front_part:
        front_product *= int(digit)
    
    back_product = 1
    for digit in back_part:
        back_product *= int(digit)
    
    if front_product == back_product:
        print("YES")
        exit()

print("NO")
