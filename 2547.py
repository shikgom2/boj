t = int(input())
x = 0
for _ in range(t):
    s = input()
    n = int(input())
    h = 0
    for i in range(n):
        h += int(input())
    if h % n == 0:    
        print("YES")
    else:
        print("NO")