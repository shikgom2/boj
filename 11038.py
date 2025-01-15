import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if line == "0 0 0":
        break
    
    m, nmin, nmax = map(int, line.split())
    
    scores = [int(input().strip()) for _ in range(m)]
    
    ans = 0
    best_gap = -1
    
    for n in range(nmin, nmax + 1):
        gap = scores[n - 1] - scores[n]
        
        if gap > best_gap:
            best_gap = gap
            ans = n
        elif gap == best_gap and n > ans:
            ans = n
    
    print(ans)
