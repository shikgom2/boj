N, C = map(int, sys.stdin.readline().split())

shows = []
for _ in range(N):
    shows.append(int(sys.stdin.readline().rstrip()))

shows.sort()

time = 0
for i in range(1, C + 1):
    for j in shows:
        if i % j == 0:
            time += 1
            break
print(time)