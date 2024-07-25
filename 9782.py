import sys
input = sys.stdin.readline

i = 0
while True:
    i += 1
    li = list(map(int, input().split()))
    if li[0] == 0:
        break

    a = li[0]
    print(f"Case {i}: ", end="")
    if a % 2 == 0:
        print("{:.1f}".format((li[a // 2] + li[a // 2 + 1]) / 2))
    else:
        print("{:.1f}".format(li[a // 2 + 1]))