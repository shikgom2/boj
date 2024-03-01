N = int(input())
fact = 1
for i in range(2, N+1):
    fact *= i
    while True:
        if str(fact)[-1] == "0":
            fact //= 10
        else:
            break
    fact %= 100000000000000
print(str(fact)[-5:])