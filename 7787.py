def prime(n):
    cnt = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    
    return cnt

i,j = map(int, input().split())

res1 = prime(i)
res2 = prime(i)

if(res1 ^ res2 == 0):
    print("A player wins")
else:
    print("B player wins")
