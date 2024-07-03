t = int(input())
for _ in range(t):
    area, base = map(float, input().split())

    ans = round(area * 2 / base, 2)
    print(f"The height of the triangle is {ans:.2f} units")