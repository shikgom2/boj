str = input()
bomb = input()
stack = []

for i in range(len(str)):
    stack.append(str[i])
    if str[i] == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if stack:
    print(''.join(stack))
else:
    print("FRULA")
