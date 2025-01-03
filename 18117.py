import sys
input = sys.stdin.readline

def modulou(base, exponent, mod):

    result = 1
    current_power = base % mod
    e = exponent
    
    while e > 0:
        if e & 1:
            result = (result * current_power) % mod
        current_power = (current_power * current_power) % mod
        e >>= 1
    
    return result


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    i, n = map(int, input().split())
    
    remain = a % b

    if i > 1:
        remain = (remain * modulou(10, i - 1, b)) % b
    
    ans = []
    for _ in range(n):
        remain *= 10
        digit = remain // b
        remain %= b
        ans.append(str(digit))
    
    print("".join(ans))
