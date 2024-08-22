import sys
input = sys.stdin.readline
def to_base_n(num, n): #n -> 10
    if num == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while num > 0:
        num, remainder = divmod(num, n)
        result = digits[remainder] + result

    return result

def from_base_n(s, n): #10 -> n
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0

    for char in s:
        value = digits.index(char)
        result = result * n + value

    return result

n,b = map(int, input().split())
print(to_base_n(n, b))