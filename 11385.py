from math import cos, sin
from functools import reduce
import operator

def xor(values):
    def xor_two_numbers(a, b):
        binary_a = format(a, 'b')
        binary_b = format(b, 'b')
        
        max_len = max(len(binary_a), len(binary_b))
        binary_a = binary_a.zfill(max_len)
        binary_b = binary_b.zfill(max_len)
        
        xor_result = ''.join(str((int(bit_a) + int(bit_b)) % 2) for bit_a, bit_b in zip(binary_a, binary_b))
        
        return int(xor_result, 2)

    return reduce(xor_two_numbers, values)

def complex_exp(theta):
    return cos(theta) + 1j * sin(theta)

def fft_manual(a, inverse=False):
    n = len(a)
    if n <= 1:
        return a
    even = fft_manual(a[0::2], inverse)
    odd = fft_manual(a[1::2], inverse)
    T = [0] * n
    for k in range(n // 2):
        if inverse:
            t = complex_exp(2 * 3.141592653589793 * k / n) * odd[k]
        else:
            t = complex_exp(-2 * 3.141592653589793 * k / n) * odd[k]
        T[k] = even[k] + t
        T[k + n // 2] = even[k] - t
    return T

def ifft_manual(a):
    n = len(a)
    a_inv = fft_manual(a, True)
    return [x / n for x in a_inv]

def fft(a, b):
    n = 1
    while n < len(a) + len(b) - 1:
        n <<= 1
    a.extend([0] * (n - len(a)))
    b.extend([0] * (n - len(b)))
    
    A = fft_manual(a)
    B = fft_manual(b)
    C = [A[i] * B[i] for i in range(n)]
    c = ifft_manual(C)
    
    c = [round(x.real) for x in c]
    
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c

N, M = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
res = fft(x,y)
res = xor(res)

print(res)
