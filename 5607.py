n = int(input())
a_score = 0
b_score = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        a_score += a + b
    elif b > a:
        b_score += a + b
    else:
        a_score += a
        b_score += b
print(a_score, b_score)
