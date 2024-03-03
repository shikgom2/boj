import math
sqrt5 = math.sqrt(5)

for k in range(1, 201):
    i = (3 + sqrt5) ** k
    print(int(i % 1000))