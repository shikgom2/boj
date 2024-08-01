import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    print(a, b, c)
    if a >= 10 and b >= 10 and c >= 10:
        print("triple-double")
    elif (a >= 10 and b >= 10) or (b >= 10 and c >= 10) or (a >= 10 and c >= 10):
        print("double-double")
    elif a >= 10 or b >= 10 or c >= 10:
        print("double")
    else:
        print("zilch")
    print()