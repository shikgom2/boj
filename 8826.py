for _ in range(int(input())):
    N = int(input().split()[0])
    S = input()
    X, Y = 0, 0
    for c in S:
        if c == 'N':
            Y += 1
        elif c == 'S':
            Y -= 1
        elif c == 'W':
            X -= 1
        elif c == 'E':
            X += 1
    print(abs(X) + abs(Y))