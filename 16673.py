c, k, p = map(int, input().split())
w = 0
for i in range(1,c+1): 
    w += i*k + p*(i**2)
print(w)