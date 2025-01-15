t = int(input())

beats = {'R': 'S', 'S': 'P', 'P': 'R'}

for _ in range(t):
    n = int(input())
    p1_wins = 0
    p2_wins = 0
    for _ in range(n):
        c1, c2 = input().split()
        if c1 == c2:
            continue
        elif beats[c1] == c2:
            p1_wins += 1
        else:
            p2_wins += 1
    if p1_wins > p2_wins:
        print("Player 1")
    elif p2_wins > p1_wins:
        print("Player 2")
    else:
        print("TIE")
