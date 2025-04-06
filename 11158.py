import sys
input = sys.stdin.readline


t = int(input().split())
for _ in range(t):
    s = input().strip()
    words = s.split()
    ans = 0
    
    for w in words:
        if w == "u" or w == "ur":
            ans += 1
        if "lol" in w:
            ans += 1
    
    for i in range(len(words) - 1):
        if words[i] in ("would", "should") and words[i + 1] == "of":
            ans += 1
    
    print(ans * 10)
