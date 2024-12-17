import sys
input = sys.stdin.readline 


def solve(N, K):
    is_erased = [False] * (N + 1)
    erase_order = []

    for P in range(2, N + 1):
        if not is_erased[P]:
            for multiple in range(P, N + 1, P):
                if not is_erased[multiple]:
                    is_erased[multiple] = True
                    erase_order.append(multiple)
                    if len(erase_order) == K:
                        return multiple
    return -1


N, K = map(int, input().split())
print(solve(N, K))
