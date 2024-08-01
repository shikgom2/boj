n = int(input())

for _ in range(n):
    li = list(map(int, input().split()))
    print(*li)
    if 17 in li and 18 in li:
        print("both")
    elif 17 in li:
        print("zack")
    elif 18 in li:
        print("mack")
    else:
        print("none")
    print()