import sys
input = sys.stdin.readline

def xor(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

def xor_range(a, b):
    return xor(b) ^ xor(a - 1)

n = int(input())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    if(b == 1):
        ans = ans ^ a
    else:
        tmp = xor_range(a, a + b - 1)
        ans = ans ^ tmp
    print(ans)

if(ans):
    print("kooasga")
else:
    print("cubelover")