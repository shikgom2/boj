def solution(D, P, Q):
    if D % P == 0 or D % Q == 0: 
        return D

    P, Q = max(P, Q), min(P, Q)
    mx_P = D // P + 1
    ans = P * mx_P

    for i in range(mx_P-1, -1, -1):
        div, mod = divmod((D - (i * P)), Q)
        if mod == 0: return D 
        mn_i = (i * P) + ((div + 1) * Q)
        if ans == mn_i: break
        ans = min(ans, mn_i)
    return ans
d, p, q = map(int, input().split())
print(solution(d,p,q))