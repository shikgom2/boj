import sys
input = sys.stdin.readline

s = input().strip()
stack = []
ans = 0

for c in s:
    if c == ' ':
        continue
    if c == '(':
        stack.append(0)
    elif c == ')':
        child = stack.pop()
        level = child + 1
        ans += level
        if stack:
            stack[-1] = max(stack[-1], level)
print(ans)
