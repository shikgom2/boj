def solve(n, numbers):
    s = []
    input_stack = []
    result = []

    for i in range(n):
        num = numbers[i]
        if not input_stack:
            input_stack.append(num)
            s.append(i + 1)
            result.append("0")
        else:
            if input_stack[-1] > num:
                result.append(str(s[-1]))
                s.append(i + 1)
                input_stack.append(num)
            else:
                s.pop()
                input_stack.pop()
                while s:
                    if input_stack[-1] > num:
                        result.append(str(s[-1]))
                        s.append(i + 1)
                        input_stack.append(num)
                        break
                    else:
                        s.pop()
                        input_stack.pop()
                if not s:
                    result.append("0")
                    s.append(i + 1)
                    input_stack.append(num)
    
    return ' '.join(result)

n = int(input())
numbers = list(map(int, input().split()))
result = solve(n, numbers)
for res in result:
    print(res, end = '')