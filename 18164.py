import sys
input = sys.stdin.readline

def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x
    
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    n = a // b
    r = a % b

    digits = []
    remainders = {}
    idx = 0
    cycle = -1

    remain = r
    while True:
        if remain == 0:
            cycle = idx
            break
        if remain in remainders:
            cycle = remainders[remain]
            break
        remainders[remain] = idx
        remain *= 2
        digit = remain // b
        digits.append(digit)
        remain = remain % b
        idx +=1

    if cycle == len(digits):
        non_repeating = digits
        repeating = []
    else:
        non_repeating = digits[:cycle]
        repeating = digits[cycle:]

    one = sum(repeating)
    total = len(repeating)

    if total == 0:
        if n > 0:
            max_numerator = 1
            max_denominator = 1
        else:
            max_numerator = sum(non_repeating)
            max_denominator = len(non_repeating)
            if max_denominator == 0:
                max_numerator = 0
                max_denominator = 1
    else:
        one = sum(repeating)
        total = len(repeating)

        g = gcd(one, total)
        ans1 = one // g
        ans2 = total // g

    print(f"{ans1}/{ans2}")


