import sys
input = sys.stdin.readline

def one():
    return min(li)

def two():
    arr = [min(li[0], li[5]), min(li[1], li[4]), min(li[2], li[3])]
    arr = sorted(arr)
    return sum(arr[:2])

def three():
    arr = [min(li[0], li[5]), min(li[1], li[4]), min(li[2], li[3])]
    arr = sorted(arr)
    return sum(arr[:])

def five():
    return sum(li) - max(li)

N = int(input())
li = list(map(int, input().split()))
res=0
if N > 2:
    res = 4 * three() + (8 * N - 12) * two() + ((N-2)**2 + 4*(N-1)*(N-2)) * one()
elif N == 2:
    res = 4 * three() + 4 * two()
else:
    res = five()
print(res)
