t = int(input())
for x in range(1, t + 1):
    m = int(input())
    
    li = []
    for _ in range(m):
        s = list(map(str, input().split()))
        li.append(s)
    flag = True
    pair = li.pop()

    mem = {pair[0]: True, pair[1]: False}

    while li:
        prev = len(li)
        for index, pair in reversed(list(enumerate(li))):
            if pair[0] in mem:
                if pair[1] in mem:
                    if mem[pair[0]] is mem[pair[1]]:
                        flag = False
                        li.clear()
                        break
                    else:
                        li.pop(index)
                else:
                    mem[pair[1]] = not mem[pair[0]]
                    li.pop(index)
            elif pair[1] in mem:
                mem[pair[0]] = not mem[pair[1]]
                li.pop(index)
        if(len(li) == prev):
            pair = li.pop()
            mem[pair[0]] = True
            mem[pair[1]] = False

    if(flag):
        flag = "Yes"
    else:
        flag = "No"

    print(f"Case #{x}: {flag}")