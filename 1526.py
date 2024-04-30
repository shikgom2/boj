n = int(input())
while(True):
    s = str(n)
    a = 0

    for i in range(len(s)):
        if(s[i] == '4' or s[i] == '7'):
            a+=1               
        else:
            n -= 1  
            continue
        
    if(a == len(s)):
        print(n)
        break