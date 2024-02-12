a,b = input().split()
result = int(a, 2) + int(b, 2)
result = bin(result)
print(result[2:])