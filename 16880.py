import sys
input = sys.stdin.readline


def grundy(x, y, c):
    if c == "R":
        return ((x // 4) ^ (y // 4)) * 4 + ((x % 4) ^ (y % 4))
    elif c == "B":
        return min(x, y)
    elif c == "K":
        return (min(x, y) % 2) * 2 + (abs(x - y) % 2)
    elif c == "N":
        r = min(x, y) % 3
        if r == 0:
            return 0
        elif r == 1:
            return 0 if x == y else 1
        elif r == 2:
            return 1 if abs(x - y) <= 1 else 2
    elif c == "P":
        # Palace: ((x//3) xor (y//3)) * 3 + ((x+y) % 3)
        return ((x // 3) ^ (y // 3)) * 3 + ((x + y) % 3)

n = int(input())
nim = 0
for _ in range(n):
    parts = input().split()
    x = int(parts[0])
    y = int(parts[1])
    c = parts[2]
    nim ^= grundy(int(x), int(y), c)
    
print("koosaga" if nim != 0 else "cubelover")
