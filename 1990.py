import math
primes = []

def is_palindrome(s):
    return s == s[::-1]

def eratosthenes(n):

    array = [True for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2 
            while i * j <= n:
                array[i * j] = False
                j += 1

    for i in range(2, n + 1):
        if array[i]:
            primes.append(i)

N,M = map(int, input().split())
if(M > 10000000):
    M = 10000000
eratosthenes(M)

for prime in primes:
    if(prime >= N):
        k = str(prime)
        if(len(k) == 1):
            print(k)
        elif(is_palindrome(k)):
             print(k)
print(-1)