t = int(input())
for i in range(1, t + 1) :
    print("Case #{:d}: {:d}".format(i, max([*map(int, input().split())])))
