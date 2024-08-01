import math

x, y = map(int, input().split())
ans = math.ceil(x * y / (4840 * 5))
print(ans)