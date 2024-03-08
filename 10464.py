def xor_mod(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

def xor(s, f):
    return xor_mod(s-1) ^ xor_mod(f)

N = int(input())
for _ in range(N):
    i,j = map(int, input().split())
    print(xor(i,j))