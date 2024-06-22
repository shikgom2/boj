def test(expression):
    result = expression[0] == 'T'
    for i in range(2, len(expression), 2):
        operator = expression[i-1]
        operand = expression[i] == 'T'
        if operator == '&':
            result = result and operand
        elif operator == '|':
            result = result or operand
    return 'T' if result else 'F'

def flip(element):
    flips = {'T': 'F', 'F': 'T', '&': '|', '|': '&'}
    return flips[element]

n = int(input())
expression = input().split()
expected_result = input()

if test(expression) == expected_result:
    print(0)
else:
    for i in range(n):
        expression[i] = flip(expression[i])
        if test(expression) == expected_result:
            print(1)
            exit()
        expression[i] = flip(expression[i])

    print(2)