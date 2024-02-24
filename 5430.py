from collections import deque

T = int(input())
while T > 0:
    T -= 1
    cmd = input()
    n = int(input())
    input_arr = input()
    dq = deque()

    num = ""
    for char in input_arr:
        if char.isdigit():
            num += char
        elif num:
            dq.append(int(num))
            num = ""
    
    ok = True
    chk = True

    for c in cmd:
        if c == 'R':
            chk = not chk
        elif c == 'D':
            if not dq:
                ok = False
                break
            else:
                if chk:
                    dq.popleft()
                else:
                    dq.pop()
    
    if not ok:
        print("error")
    else:
        result = []
        while dq:
            if chk:
                result.append(dq.popleft())
            else:
                result.append(dq.pop())
        print("[" + ",".join(map(str, result)) + "]")