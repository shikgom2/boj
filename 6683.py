def calc_leftover_cuts(gw, gh, W, H):
    # gw,gh is block size; W,H is sheet size
    # Determine leftover cuts needed
    match_width = (gw == W)
    match_height = (gh == H)

    if match_width and match_height:
        return 0
    elif match_width and gh < H:
        return 1
    elif match_height and gw < W:
        return 1
    else:
        # gw < W and gh < H
        return 2

while True:
    A,B,C,D,E,F = map(int, input().split())
    if A==0 and B==0 and C==0 and D==0 and E==0 and F==0:
        break

    # Four possible orientations
    orientations = [
        (A*C, B*D),
        (A*D, B*C),
        (B*C, A*D),
        (B*D, A*C)
    ]
    
    best = None  # track minimal number of cuts

    for (gw, gh) in orientations:
        for (W, H) in [(E,F), (F,E)]:  
            # Try fitting (gw, gh) into (W, H) without rotation
            if gw <= W and gh <= H:
                leftover = calc_leftover_cuts(gw, gh, W, H)
                total = leftover + (A*B - 1)
                if best is None or total < best:
                    best = total
            
            # Try fitting (gh, gw) rotated into (W, H)
            if gh <= W and gw <= H:
                leftover = calc_leftover_cuts(gh, gw, W, H)
                total = leftover + (A*B - 1)
                if best is None or total < best:
                    best = total

    if best is None:
        print("The paper is too small.")
    else:
        print(f"The minimum number of cuts is {best}.")