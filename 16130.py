import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    cum = 0
    curr_q = 0
    week = 0
    ans = None
    
    for ch in s:
        if ans is not None:
            break
            
        if ch.isdigit():
            points = int(ch)
        else:
            points = ord(ch) - ord('A') + 10
            
        new_cum = cum + points
        new_q = new_cum // 10
        
        if new_q > curr_q:
            if new_q < 4:
                week += new_q
            elif new_q == 4:
                ans = "weapon"
            else:
                ans = "09"
            cum = new_cum
            curr_q = new_q
        else:
            cum = new_cum
    
    if ans is None:
        print(week)
    else:
        print(f"{week}({ans})")