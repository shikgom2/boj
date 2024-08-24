while True:
    s = input()
    left_list = []
    error = 0
    i = 0
    if s[0] == ".":
        break
    
    while True:
        a = s[i]
        if a == ".":
            if len(left_list) > 0:
                error += 1
            break
            
        if a == "[" or a == "(":
            left_list.append(a)
        
        elif a == "]":
            try:
                b = left_list.pop()
            except:
                error += 1
                break
            
            if b == "[":
                pass
            else:
                error += 1
                
        elif a == ")":
            try:
                b = left_list.pop()
            except:
                error += 1
                break
                
            if b == "(":
                pass
            else:
                error += 1
        i += 1
    
    if error == 0:
        print("yes")
    else:
        print("no")