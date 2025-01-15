n = int(input())
for _ in range(n):
    s = input().strip()
    length = len(s)
    first = s[length//2 - 1]
    second = s[length//2]
    if first == second:
        print("Do-it")
    else:
        print("Do-it-Not")
