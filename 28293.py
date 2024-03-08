import math
n,m = map(int, input().split())
print(math.floor(m * math.log10(n)) + 1)