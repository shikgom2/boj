a, b = map(int, input().split())

if a / b < 0.2:
    print("weak")
elif a / b < 0.4:
    print("normal")
elif a / b < 0.6:
    print("strong")
else:
    print("very strong")