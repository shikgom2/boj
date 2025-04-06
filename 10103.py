import sys
input = sys.stdin.readline

n = int(input())
score1 = 100
score2 = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        score2 -= a
    elif b > a:
        score1 -= b
print(score1)
print(score2)