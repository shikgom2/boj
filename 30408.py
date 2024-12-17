import sys
input = sys.stdin.readline

n,m = map(int, input().split())

stack = [n]
visited = set()

while stack:
    current = stack.pop()
    
    if current == m:
        print("YES")
        exit()
    
    if current < m or current in visited:
        continue
    
    visited.add(current)
    
    if current == 1:
        continue
    if current % 2 == 0:
        next_val = current // 2
        stack.append(next_val)
    else:
        lower = (current - 1) // 2
        upper = lower + 1
        stack.append(lower)
        stack.append(upper)

print("NO")
