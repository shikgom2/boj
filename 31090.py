t = int(input())
for _ in range(t):
    n = int(input())
    if (n + 1) % (n % 100) == 0:
        print("Good")
    else:
        print("Bye")