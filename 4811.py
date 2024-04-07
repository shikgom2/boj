import math

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def catalan_number(n):
    return binomial_coefficient(2*n, n) // (n + 1)

while(True):
    n = int(input())
    if(n == 0):
        break
    else:
        print(catalan_number(n))
