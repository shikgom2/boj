fibo = [0] * 51
fibo[0] = 0
fibo[1] = 1

for i in range(2, 51):
    fibo[i] = fibo[i-1] + fibo[i-2]

fibo.reverse()

t = int(input())
for _ in range(t):
    n = int(input())
    tmp = []

    for i in range(51):
        if(fibo[i] <= n):
            tmp.append(fibo[i])
            n -= fibo[i]
        
        if(n == 0):
            break
    tmp.reverse()
    print(*tmp)
