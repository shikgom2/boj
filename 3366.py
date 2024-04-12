import sys
input = sys.stdin.readline

n = int(input())

li = []
game = []

#Input
for _ in range(n):
    i = int(input())
    li.append(i)
    game.append(i)
#sort
li.sort()

#boring score
res = 0
for i in range(n - 1):
    #get min elements this round
    worst = li[i] 

    for idx, val in enumerate(game):
        if val == worst:
            #compare to right
            if idx == 0:
                right = game[idx + 1]
                res += max(worst, right)
            #compare to left
            elif idx == len(game) - 1:
                left = game[idx - 1]
                res += max(worst, left)
            #get right & left and gets min element
            else:
                right = game[idx + 1]
                left = game[idx - 1]
                res += max(worst, left, right)

            #delete game
            game.pop(idx)
            break

print(res)