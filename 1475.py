import sys
input = sys.stdin.readline

n = int(input())
check = [0] * 10

while(n):
    i = n % 10
    check[i] += 1
    n //= 10

check[6] += check[9]
check[9] = 0

if(check[6] % 2):
    check[6] = check[6] // 2 + 1
else:
    check[6] //= 2

print(max(check))