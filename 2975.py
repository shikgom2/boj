while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    
    if a == 0 and op == 'W' and b == 0:
        break
    
    if op == 'D':
        ans = a + b
        print(ans)
    elif op == 'W':
        if a - b >= -200:
            ans = a - b
            print(ans)
        else:
            print("Not allowed")
