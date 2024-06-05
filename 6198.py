n = int(input())
bld = [0] * 80080
for i in range(n):
    bld[i] = int(input())
    
stack = []
ans = 0
for i in range(n):
    while stack and bld[stack[-1]] <= bld[i]:
        stack.pop()
    ans += len(stack)
    stack.append(i)

print(ans)