n,m,k,a,b,c=map(int, input().split())
x = max((n*a), (m*b), (k*c))

if (n * a == x):
    print("Joffrey",end=" ")
if (m * b == x):
    print("Robb", end=" ")
if (k * c == x):
    print("Stannis")