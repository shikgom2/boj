import sys
input = sys.stdin.readline

n,m = map(int, input().split())
track = [0]
li = []
joker = 0

for _ in range(m):
    a,b = map(int, input().split())

    if(a == 1):
        joker = (b + joker) % n
    elif(a == 2):
        joker = (joker - b)
        if(joker < 0):
            joker = (joker + n) % n
    elif(a == 3):
        joker = track[b]
    
    track.append(joker)

print(joker+1)