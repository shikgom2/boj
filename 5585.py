n = int(input())
n = 1000 - n
res = 0
res += (n // 500)
n %= 500
res += (n // 100)
n %= 100
res += (n // 50)
n %= 50
res += (n // 10)
n %= 10
res += (n // 5)
n %= 5
res += n
print(res)