import sys
from functools import lru_cache

MOD = 104857601
PR = 3

class MINT:
    def __init__(self, v=0):
        self.v = v % MOD

    def __add__(self, other):
        return MINT(self.v + other.v)

    def __sub__(self, other):
        return MINT(self.v - other.v)

    def __mul__(self, other):
        return MINT(self.v * other.v)

    def __truediv__(self, other):
        return self * MINT.pow(other, MOD - 2)

    @staticmethod
    def pow(a, b):
        result = MINT(1)
        base = a
        while b > 0:
            if b & 1:
                result *= base
            base *= base
            b >>= 1
        return result

    def __neg__(self):
        return MINT(-self.v)

    def __repr__(self):
        return f"{self.v}"

class FFT:
    def __init__(self, prime, primitive_root):
        self.P = prime
        self.PR = primitive_root
        self.PRI = MINT.inv(MINT(primitive_root))
        self.MSZ = (prime - 1) & (1 - prime)
        self.W = MINT.pow(MINT(primitive_root), (prime - 1) // self.MSZ)
        self.WI = MINT.pow(self.PRI, (prime - 1) // self.MSZ)

    def fft(self, sz, a, inv):
        w = MINT.pow(self.WI if inv else self.W, self.MSZ // sz)
        ssz = sz >> 1
        while ssz:
            for i in range(0, sz, ssz << 1):
                wt = MINT(1)
                for j in range(ssz):
                    lft = a[i + j]
                    rgh = a[i + j + ssz]
                    lftold = lft
                    a[i + j] = lft + rgh
                    a[i + j + ssz] = (lftold - rgh) * wt
                    wt *= w
            w *= w
            ssz >>= 1
        if inv:
            invsz = MINT.inv(MINT(sz))
            for i in range(sz):
                a[i] *= invsz
        j = 0
        for i in range(1, sz):
            dg = sz >> 1
            while j & dg:
                j ^= dg
                dg >>= 1
            j ^= dg
            if i < j:
                a[i], a[j] = a[j], a[i]

    def convolution(self, a, b):
        sz = len(a) + len(b)
        fftsz = sz
        while fftsz & (fftsz - 1):
            fftsz += fftsz & -fftsz
        av = [MINT(0)] * fftsz
        bv = [MINT(0)] * fftsz
        for i in range(len(a)):
            av[i] = a[i]
        for i in range(len(b)):
            bv[i] = b[i]
        self.fft(fftsz, av, False)
        self.fft(fftsz, bv, False)
        for i in range(fftsz):
            av[i] *= bv[i]
        self.fft(fftsz, av, True)
        return av

class Poly:
    def __init__(self, coeffs):
        self.coeffs = [MINT(x) for x in coeffs]
        self.normalize()

    def normalize(self):
        while self.coeffs and self.coeffs[-1].v == 0:
            self.coeffs.pop()

    def __add__(self, other):
        new_coeffs = [MINT(0)] * max(len(self.coeffs), len(other.coeffs))
        for i in range(len(new_coeffs)):
            if i < len(self.coeffs):
                new_coeffs[i] += self.coeffs[i]
            if i < len(other.coeffs):
                new_coeffs[i] += other.coeffs[i]
        return Poly(new_coeffs)

    def __sub__(self, other):
        new_coeffs = [MINT(0)] * max(len(self.coeffs), len(other.coeffs))
        for i in range(len(new_coeffs)):
            if i < len(self.coeffs):
                new_coeffs[i] += self.coeffs[i]
            if i < len(other.coeffs):
                new_coeffs[i] -= other.coeffs[i]
        return Poly(new_coeffs)

    def __mul__(self, other):
        new_coeffs = [MINT(0)] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                new_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]
        return Poly(new_coeffs)

    def mod(self, mod_poly):
        # Assume mod_poly's highest degree coefficient is 1
        k = len(mod_poly.coeffs)
        while len(self.coeffs) >= k:
            factor = self.coeffs[-1]
            degree_diff = len(self.coeffs) - k
            for i in range(k):
                self.coeffs[degree_diff + i] -= mod_poly.coeffs[i] * factor
            self.normalize()
        return self

    def __repr__(self):
        return "Poly([" + ", ".join(str(x) for x in self.coeffs) + "])"
    
def main():
    input = sys.stdin.read
    data = input().split()
    K, N = map(int, data[0:2])
    A = list(map(int, data[2:2 + K]))
    B = list(map(int, data[2 + K:2 + 2 * K]))

    # Convert B to negative and add 1 at the end for the polynomial
    B = [-b for b in B]
    B.append(1)
    polyB = Poly(B)

    # Polynomial A
    polyA = Poly(A)

    if N < K:
        print(A[N])
        return

    # Fast exponentiation of the polynomial x^n mod polyB
    result_poly = Poly([1])  # This is x^0
    x_poly = Poly([0, 1])   # This is x^1
    n = N - 1

    while n > 0:
        if n % 2 == 1:
            result_poly = (result_poly * x_poly).mod(polyB)
        x_poly = (x_poly * x_poly).mod(polyB)
        n //= 2

    # Calculate the result by evaluating the polynomial at polyA
    result = MINT(0)
    for i in range(min(len(result_poly.coeffs), len(polyA.coeffs))):
        result += result_poly.coeffs[i] * polyA.coeffs[i]
    print(result)

if __name__ == "__main__":
    main()

