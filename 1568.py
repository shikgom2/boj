N = int(input())

res = 0
song = 0
fly = 0
while True:
    res += 1
    song += 1
    if fly + song > N:
        song = 1
    fly += song
    if fly == N:
        break
print(res)