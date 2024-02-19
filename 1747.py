import math

def is_palindrome(s):
    return s == s[::-1]

def isPrime(n):
    array = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2 
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array

N = int(input())
result = isPrime(N)
  
end, sum_, cnt = 2, 0, 0

for start in range(2, N+1):
    if not result[start]: continue
    while sum_ < N and end < N+1:
        if not result[end]: 
            end += 1
            continue
        sum_ += end
        end += 1
    if sum_ == N: 
        cnt += 1
    sum_ -= start
    
print(cnt)