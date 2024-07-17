a = int(input())
b = int(input())
k = int(input())
    
for i in range(a, b + 1):
    for k in range(1, min(k, i) + 1):
        print(i * (i - 1) // 2 + k, end=' ')
    print()