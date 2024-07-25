n = int(input())
k = int(input())
k+= 60
if n <= k:
    print(n * 1500)
else:
    print(n * 3000 - k * 1500)