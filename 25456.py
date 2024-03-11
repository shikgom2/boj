from math import cos, sin

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

N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
y.reverse()
print(max(fft(x+x, y)))