T = int(input())
for _ in range(T):
    pos, s = input().split()
    pos = int(pos)
    ans = s[:pos-1] + s[pos:]
    print(ans)
