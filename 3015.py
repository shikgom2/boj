import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = 0

for _ in range(n):
    x = int(input())

    while stack and stack[-1][0] < x:
        ans += stack[-1][1]
        stack.pop() 

    val = 1
    if stack and stack[-1][0] == x:
        val += stack[-1][1]
        ans += stack[-1][1]
        stack.pop()

    if stack:
        ans += 1

    stack.append((x, val))
print(ans)
