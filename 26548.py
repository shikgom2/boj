import math

t = int(input())

for _ in range(t):
    a, b, c = map(float, input().split())
    d = b**2 - 4 * a * c
    
    ans1 = (-b + math.sqrt(d)) / (2 * a)
    ans2 = (-b - math.sqrt(d)) / (2 * a)
    
    print(f"{ans1:.3f}, {ans2:.3f}")
