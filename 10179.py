import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    s = float(input())
    print(f"${s * 0.8:.2f}")