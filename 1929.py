primes = []
def eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        # p가 소수인 경우, p의 배수를 소수가 아니라고 표시합니다.
        if (prime[p] == True):
            # p의 배수들을 False로 설정합니다.
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
           primes.append(p)

N,M = map(int, input().split())
eratosthenes(M)

for prime in primes:
    if(prime >= N):
        print(prime)