import sys
input = sys.stdin.readline

def solve(li):
    for i in li:
        if sorted(i) != list(range(1, 10)):
            return False

    for c in range(9):
        col = [li[r][c] for r in range(9)]
        if sorted(col) != list(range(1, 10)):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = []
            for k in range(3):
                for l in range(3):
                    block.append(li[i+k][j+l])
            if sorted(block) != list(range(1, 10)):
                return False

    return True

t = int(input())
for i in range(1, t+1):
    li = []
    while len(li) < 9:
        line = input().strip()
        if not line:
            continue
        li.append(list(map(int, line.split())))

    result = "CORRECT" if solve(li) else "INCORRECT"
    print(f"Case {i}: {result}")