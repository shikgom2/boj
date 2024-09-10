MOD1 = 998244353
MOD2 = 985661441
MOD3 = 943718401
MOD4 = 935329793
MOD5 = 918552577

mod1 = lambda : MOD1
mod2 = lambda : MOD2
mod3 = lambda : MOD3
mod4 = lambda : MOD4
mod5 = lambda : MOD5

def primitive_root(m):
    if m == 2: return 1
    if m == 167772161: return 3
    if m == 469762049: return 3
    if m == 754974721: return 11
    if m == 998244353: return 3
    divs = [0] * 20
    divs[0] = 2
    cnt = 1
    x = (m - 1) // 2
    while x % 2 == 0: x //= 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            divs[cnt] = i
            cnt += 1
            while x % i == 0: x //= i
        i += 2
    if x > 1:
        divs[cnt] = x
        cnt += 1
    g = 2
    while True:
        for i in range(cnt):
            if pow(g, (m - 1) // divs[i], m) == 1: break
        else:
            return g
        g += 1

def popcount(x):
    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)
    x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)
    x = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)
    x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)
    x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)
    return x

def tzcount(x):
    return popcount(~x & (x - 1))

def build_ntt(mod):
    g = primitive_root(mod())
    rank2 = tzcount(mod() - 1)
    root = [0] * (rank2 + 1)
    iroot = [0] * (rank2 + 1)
    rate2 = [0] * max(0, rank2 - 1)
    irate2 = [0] * max(0, rank2 - 1)
    rate3 = [0] * max(0, rank2 - 2)
    irate3 = [0] * max(0, rank2 - 2)
    root[rank2] = pow(g, (mod() - 1) >> rank2, mod())
    iroot[rank2] = pow(root[rank2], mod() - 2, mod())
    for i in range(rank2)[::-1]:
        root[i] = root[i + 1] * root[i + 1]
        root[i] %= mod()
        iroot[i] = iroot[i + 1] * iroot[i + 1]
        iroot[i] %= mod()
    prod = 1
    iprod = 1
    for i in range(rank2 - 1):
        rate2[i] = root[i + 2] * prod % mod()
        irate2[i] = iroot[i + 2] * iprod % mod()
        prod *= iroot[i + 2]
        prod %= mod()
        iprod *= root[i + 2]
        iprod %= mod()
    prod = 1
    iprod = 1
    for i in range(rank2 - 2):
        rate3[i] = root[i + 3] * prod % mod()
        irate3[i] = iroot[i + 3] * iprod % mod()
        prod *= iroot[i + 3]
        prod %= mod()
        iprod *= root[i + 3]
        iprod %= mod()
    return root, iroot, rate2, irate2, rate3, irate3

def butterfly(a, mod, rate2, irate2, rate3, irate3, imag, iimag):
    n = len(a)
    h = (n - 1).bit_length()
    len_ = 0
    while len_ < h:
        if h - len_ == 1:
            p = 1 << (h - len_ - 1)
            rot = 1
            for s in range(1 << len_):
                offset = s << (h - len_)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p] * rot % mod()
                    a[i + offset] = (l + r) % mod()
                    a[i + offset + p] = (l - r) % mod()
                if s + 1 != 1 << len_:
                    rot *= rate2[(~s & -~s).bit_length() - 1]
                    rot %= mod()
            len_ += 1
        else:
            p = 1 << (h - len_ - 2)
            rot = 1
            for s in range(1 << len_):
                rot2 = rot * rot % mod()
                rot3 = rot2 * rot % mod()
                offset = s << (h - len_)
                for i in range(p):
                    a0 = a[i + offset]
                    a1 = a[i + offset + p] * rot
                    a2 = a[i + offset + p * 2] * rot2
                    a3 = a[i + offset + p * 3] * rot3
                    a1na3imag = (a1 - a3) % mod() * imag
                    a[i + offset] = (a0 + a2 + a1 + a3) % mod()
                    a[i + offset + p] = (a0 + a2 - a1 - a3) % mod()
                    a[i + offset + p * 2] = (a0 - a2 + a1na3imag) % mod()
                    a[i + offset + p * 3] = (a0 - a2 - a1na3imag) % mod()
                if s + 1 != 1 << len_:
                    rot *= rate3[(~s & -~s).bit_length() - 1]
                    rot %= mod()
            len_ += 2

def butterfly_inv(a, mod, rate2, irate2, rate3, irate3, imag, iimag):
    n = len(a)
    h = (n - 1).bit_length()
    len_ = h
    while len_:
        if len_ == 1:
            p = 1 << (h - len_)
            irot = 1
            for s in range(1 << (len_ - 1)):
                offset = s << (h - len_ + 1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p]
                    a[i + offset] = (l + r) % mod()
                    a[i + offset + p] = (l - r) * irot % mod()
                if s + 1 != (1 << (len_ - 1)):
                    irot *= irate2[(~s & -~s).bit_length() - 1]
                    irot %= mod()
            len_ -= 1
        else:
            p = 1 << (h - len_)
            irot = 1
            for s in range(1 << (len_ - 2)):
                irot2 = irot * irot % mod()
                irot3 = irot2 * irot % mod()
                offset = s << (h - len_ + 2)
                for i in range(p):
                    a0 = a[i + offset]
                    a1 = a[i + offset + p]
                    a2 = a[i + offset + p * 2]
                    a3 = a[i + offset + p * 3]
                    a2na3iimag = (a2 - a3) * iimag % mod()
                    a[i + offset] = (a0 + a1 + a2 + a3) % mod()
                    a[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % mod()
                    a[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 % mod()
                    a[i + offset + p * 3] = (a0 - a1 - a2na3iimag) * irot3 % mod()
                if s + 1 != (1 << (len_ - 2)):
                    irot *= irate3[(~s & -~s).bit_length() - 1]
                    irot %= mod()
            len_ -= 2

def convolution(a, b, mod):
    root, iroot, rate2, irate2, rate3, irate3 = build_ntt(mod)
    imag = root[2]
    iimag = iroot[2]
    n = len(a)
    m = len(b)
    if not n or not m: return []
    if min(n, m) <= 100:
        if n < m:
            n, m = m, n
            a, b = b, a
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i + j] += a[i] * b[j]
                res[i + j] %= mod()
        return res
    z = 1 << (n + m - 2).bit_length()
    a += [0] * (z - n)
    b += [0] * (z - m)
    butterfly(a, mod, rate2, irate2, rate3, irate3, imag, iimag)
    butterfly(b, mod, rate2, irate2, rate3, irate3, imag, iimag)
    for i in range(z):
        a[i] *= b[i]
        a[i] %= mod()
    butterfly_inv(a, mod, rate2, irate2, rate3, irate3, imag, iimag)
    a = a[:n + m - 1]
    iz = pow(z, mod() - 2, mod())
    for i in range(n + m - 1):
        a[i] *= iz
        a[i] %= mod()
    return a

def inv_gcd(a, b):
    a %= b
    if a == 0: return b, 0
    s = b
    t = a
    m0 = 0
    m1 = 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0
    if m0 < 0: m0 += b // s
    return s, m0

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def crt_garner(rs, ms):
    assert len(rs) == len(ms)
    mask = 18446744073709551615
    rs = list(rs)
    ms = list(ms)
    n = len(rs)
    for i in range(n):
        for j in range(i):
            g = gcd(ms[i], ms[j])
            if (rs[j] - rs[i]) % g:
                return -1, -1
            ms[i] //= g
            ms[j] //= g
            gi = gcd(ms[i], g)
            gj = g // gi
            while True:
                g = gcd(gi, gj)
                if g == 1: break
                gi *= g
                gj //= g
            ms[i] *= gi
            ms[j] *= gj
            rs[i] %= ms[i]
            rs[j] %= ms[j]
    lcm = 1
    for i in range(n):
        lcm *= ms[i]
        lcm &= mask
    res = rs[0]
    m_mul = 1
    t = [0] * n
    for i in range(1, n):
        x_mod = rs[0] % ms[i]
        m_mul_mod = 1
        for j in range(1, i):
            m_mul_mod *= ms[j - 1]
            m_mul_mod %= ms[i]
            x_mod += m_mul_mod * t[j]
            x_mod %= ms[i]
        m_inv_mod = 1
        for j in range(i):
            s, m = inv_gcd(ms[j], ms[i])
            m_inv_mod *= m
            m_inv_mod %= ms[i]
        t[i] = (rs[i] - x_mod) % ms[i] * m_inv_mod % ms[i]
        m_mul *= ms[i - 1]
        m_mul &= mask
        res += t[i] * m_mul
        res &= mask
    return res, lcm

def crt(r, m):
    assert len(r) == len(m)
    n = len(r)
    r0 = 0
    m0 = 1
    for i in range(n):
        assert 1 <= m[i]
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1: return 0, 0
            continue
        g, im = inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1 - r0) % g: return 0, 0
        x = (r1 - r0) // g * im % u1
        r0 += x * m0
        m0 *= u1
        if (r0 < 0): r0 += m0
    return r0, m0

def convolution_64bit(a, b):
    n = len(a)
    m = len(b)
    mask = 18446744073709551615
    mods = (MOD1, MOD2, MOD3, MOD4, MOD5)
    c1 = convolution([v % MOD1 for v in a], [v % MOD1 for v in b], mod1)[:n + m - 1]
    c2 = convolution([v % MOD2 for v in a], [v % MOD2 for v in b], mod2)[:n + m - 1]
    c3 = convolution([v % MOD3 for v in a], [v % MOD3 for v in b], mod3)[:n + m - 1]
    c4 = convolution([v % MOD4 for v in a], [v % MOD4 for v in b], mod4)[:n + m - 1]
    c5 = convolution([v % MOD5 for v in a], [v % MOD5 for v in b], mod5)[:n + m - 1]
    res = [0] * (n + m - 1)
    for i, v in enumerate(zip(c1, c2, c3, c4, c5)):
        cr, cm = crt(v, mods)
        res[i] += cr
        res[i] &= mask
    return res


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = convolution_64bit(A, B)

ans = 0
for i in range(len(C)):
    ans ^= C[i]
print(ans)