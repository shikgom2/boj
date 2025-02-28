import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dp(i, stackA, stackB, dA, dB, arr, occ, total):
    if i == total:
        if stackA == () and stackB == ():
            return dA + dB
        else:
            return float('inf')
    color = arr[i]
    is_second = (occ[i] == 1)
    best = float('inf')
    if not is_second:
        # 첫 등장: 위쪽 또는 아래쪽에 추가
        new_stackA = stackA + (color,)
        new_dA = max(dA, len(new_stackA))
        best = min(best, dp(i+1, new_stackA, stackB, new_dA, dB, arr, occ, total))
        new_stackB = stackB + (color,)
        new_dB = max(dB, len(new_stackB))
        best = min(best, dp(i+1, stackA, new_stackB, dA, new_dB, arr, occ, total))
    else:
        # 두 번째 등장: 해당 색이 스택의 최상단에 있어야 함
        if stackA and stackA[-1] == color:
            best = min(best, dp(i+1, stackA[:-1], stackB, dA, dB, arr, occ, total))
        if stackB and stackB[-1] == color:
            best = min(best, dp(i+1, stackA, stackB[:-1], dA, dB, arr, occ, total))
    return best

def solve():
    n = int(input().strip())
    li = input().split()
    dic = {}
    index_counter = 0
    arr = []
    occ = [None] * (2*n)
    first = {}
    
    for i, color in enumerate(li):
        if color not in dic:
            dic[color] = index_counter
            index_counter += 1
        idx = dic[color]
        arr.append(idx)
        if idx not in first:
            first[idx] = i
            occ[i] = 0   # 첫 등장
        else:
            occ[i] = 1   # 두 번째 등장

    total = 2 * n
    arr = tuple(arr)
    occ = tuple(occ)

    ans = dp(0, (), (), 0, 0, arr, occ, total)
    return -1 if ans == float('inf') else ans


t = int(input())
for i in range(1, t+1):
    print(f"Case #{i}: {solve()}")
