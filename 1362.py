import sys
input = sys.stdin.readline

tt = 1
while True:
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break

    dead = False
    while True:
        line = input().strip()
        if line == "# 0":
            break

        if dead:
            continue

        cmd, n_str = line.split()
        n = int(n_str)
        if cmd == 'E':
            w -= n
        elif cmd == 'F':
            w += n

        if w <= 0:
            dead = True

    if dead:
        ans = "RIP"
    elif o / 2 < w < 2 * o:
        ans = ":-)"
    else:
        ans = ":-("

    print(f"{tt} {ans}")
    tt += 1