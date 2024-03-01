s = list(input())
stack = []
ans = ''

for t in s:
    if t.isalpha():
        ans += t
    elif t == '(':
        stack.append(t)
    elif t == '*' or t == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(t)
    elif t == '+' or t == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(t)
    else:
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
while stack:
    ans += stack.pop()
print(ans)
