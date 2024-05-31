n = int(input())
if n >= 1:
    li = [1, 1, 1, 1, 2, 1]
    k = (n - 1) // 6
    m = (n - 1) % 6
    
    ans = 0
    for i in range(m):
        ans = ans + li[i] + k
    print(3 * k * k + 4 * k + ans + 1)