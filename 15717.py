N = int(input())
N -= 1
ans = 1
x = 2
MOD = 1000000007

while(N > 0):
    if(N % 2 == 1):
        ans = (ans * x) % MOD

    x = (x * x) % MOD
    N = N // 2
print(ans)