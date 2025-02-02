def parse_time(t):
    hh, mm, ss = map(int, t.split(':'))
    return hh * 3600 + mm * 60 + ss

def clock_int(h,m,s):
    return h * 10000 + m * 100 + s

def solve(s, e):
    count = 0
    current = s
    while True:
        h = current // 3600
        remain = current % 3600
        m = remain // 60
        s = remain % 60
        
        c_int = clock_int(h, m, s)
        if c_int % 3 == 0:
            count += 1
        
        if current == e:
            break
        
        current = (current + 1) % 86400
    
    return count

for _ in range(3):
    line = input().strip()
    start_str, end_str = line.split()
    
    s = parse_time(start_str)
    e = parse_time(end_str)

    print(solve(s, e))
