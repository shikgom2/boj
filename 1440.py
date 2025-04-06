import sys
input = sys.stdin.readline

s = input().strip()
parts = s.split(':')

ps = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [1, 2, 0],
    [2, 0, 1],
    [2, 1, 0]
]

ans = 0
for p in ps:
    hour = int(parts[p[0]])
    minute = int(parts[p[1]])
    second = int(parts[p[2]])
    
    if 1 <= hour <= 12 and 0 <= minute <= 59 and 0 <= second <= 59:
        ans += 1

print(ans)