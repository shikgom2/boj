n = int(input())

for _ in range(n):
    s, i, j = input().split()
    li = [a for a in range(int(i), int(j))]

    for b in range(len(s)):
        if b not in li:
            print(s[b], end="")
    print()