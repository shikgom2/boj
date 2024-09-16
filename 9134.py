import sys
input = sys.stdin.readline

def code(a, b, c):
    return (a << 12) + (b << 6) + c

SYNTAX = 0
komp = [-1] * (64 * 64 * 64)
velk = [1] * (64 * 64 * 64)
s = [''] * (64*64*64*5)

def repr(p):
    if komp[p] == -1:
        return p
    komp[p] = repr(komp[p])
    return komp[p]

def join(p, q):
    P = repr(p)
    Q = repr(q)
    if P == Q:
        return
    if velk[P] < velk[Q]:
        velk[Q] += velk[P]
        komp[P] = Q
    else:
        velk[P] += velk[Q]
        komp[Q] = P

for line in sys.stdin:
    s = line.strip()
    if not s:
        break
    h, x, y = map(int, s.split())
    
    while h and x and y:
        for i in range(h):
            for j in range(x):
                for k in range(y):
                    l = code(i, j, k)
                    komp[l] = -1
                    velk[l] = 1
        l0 = 0
        for i in range(h):
            for j in range(x):
                s = input().strip()
                k = len(s)
                s += '\0' * (2 * y - k)
                for k in range(y - 1):
                    if s[1 + 2 * k] == '-':
                        join(code(i, j, k), code(i, j, k + 1))
                s = input().strip()
                if j == x - 1:
                    continue
                k = len(s)
                s += '\0' * (2 * y - k)
                for k in range(y):
                    if s[2 * k] == '|':
                        join(code(i, j, k), code(i, j + 1, k))
            if i == h - 1:
                continue
            l = 1
            for j in range(x):
                s = input().strip()
                k = len(s)
                s += '\0' * (2 * y - k)
                for k in range(y):
                    if s[2 * k] == 'o':
                        l = 0
                        join(code(i, j, k), code(i + 1, j, k))
                s = input().strip()
            if l:
                l0 += 1
        l = -1
        for i in range(h):
            for j in range(x):
                for k in range(y):
                    if komp[code(i, j, k)] == -1:
                        l += 1
        if l:
            if l + l0 >= 1000:
                print(f"Ocekavana cena: {((l + l0) // 1000)},{((l + l0) % 1000):03d},000 Kc")
            else:
                print(f"Ocekavana cena: {l + l0},000 Kc")
        else:
            print("Budova je jiz dostatecne propojena.")
        s = input().strip()
        h, x, y = map(int, s.split())

