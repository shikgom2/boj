a, b, c = map(int, input().split())
a = a * 0.229 * 0.324
b = b * 0.297 * 0.42
c = c * 0.21 * 0.297
print(2 * a + 2 * b + c)