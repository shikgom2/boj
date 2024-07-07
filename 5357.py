import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().rstrip()

    cur = ""
    for i in range(len(s)): 
        if(cur != s[i]):
            print(s[i], end="")
            cur = s[i]
    
    print("")