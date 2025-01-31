import math

while True:
    try:
        line = input().strip()
        if not line:
            continue
        tokens = line.split()
        W = int(tokens[1])
        AR = int(tokens[3])
        RD = int(tokens[-1])

        OD_cm = RD * 2.54 + 2 * W * AR / 1000
        C_cm = math.pi * OD_cm

        C_rounded = int(C_cm + 0.5)

        print(f"{line}: {C_rounded}")

    except EOFError:
        break
