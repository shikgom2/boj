n = int(input())

for _ in range(n):
    i, f = map(int, input().split())

    if i <= 2 and f <= 1:
        print("Yes")
    elif i <= 1 and f <= 2:
        print("Yes")
    else:
        print("No")