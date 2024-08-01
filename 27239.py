n = int(input())
a, b = divmod(n, 8)
if b == 0:
    b = 8
    a -= 1
print(f"{chr(b+96)}{a+1}")