import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    li = input().rstrip('\n')
    
    if not li:  
        print(1)
        continue
    
    stack = []
    cur = 0
    depth = 0
    
    for ch in li:
        if ch == '[':
            stack.append(ch)
            cur += 1
            depth = max(depth, cur)
        elif ch == ']':
            if stack:
                stack.pop()
                cur -= 1
    
    print(2 ** depth)
