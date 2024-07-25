import sys
input = sys.stdin.readline

H1, M1, S1 = map(int, input().split(" : "))
H2, M2, S2 = map(int, input().split(" : "))
ans = 0
if S2 < S1:
    ans += 60 + S2 - S1
    M2 -= 1
else:
    ans += S2 - S1
if M2 < M1:
    ans += 3600 + 60 * (M2 - M1)
    H2 -= 1
else:
    ans += 60 * (M2 - M1)

if H2 < H1:
    H2 += 24
ans += 3600 * (H2 - H1)
print(ans)