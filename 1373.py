octal = input()
decimal = int(octal, 8)
binary = bin(decimal)[2:]
print(binary)