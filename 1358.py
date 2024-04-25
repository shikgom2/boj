import math
W, H, X, Y, P = map(int, input().split())
ans = 0

for _ in range(P):
    a, b = map(int, input().split())
    
    if ((a - X)**2 + (b - (Y + H / 2))**2 <= (H / 2)**2) and a < X:
        ans += 1
    elif X <= a <= X + W and Y <= b <= Y + H:
        ans += 1
    elif ((a - (X + W))**2 + (b - (Y + H / 2))**2 <= (H / 2)**2) and X + W < a:
        ans += 1

print(ans)