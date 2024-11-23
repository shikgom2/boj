import sys
input = sys.stdin.readline

def check(before, move):
    dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
    
    befor_num = dic[before[0]]
    move_num = dic[move[0]]
    
    if abs(move_num - befor_num) == 2 and abs(int(move[1]) - int(before[1])) == 1 and not visited[move_num][int(move[1])-1]:
        visited[move_num][int(move[1])-1] = True
    elif abs(move_num - befor_num) == 1 and abs(int(move[1]) - int(before[1])) == 2 and not visited[move_num][int(move[1])-1]:
        visited[move_num][int(move[1])-1] = True
    else:
        return False
    return True

flag = True
visited = [[False for _ in range(6)] for _ in range(6)]

for i in range(36):
    move = input().strip()
    
    if i == 0:
        start = move
    else:
        if not check(before, move):
            flag = False
            break
    before = move
    
if not check(before, start):
    flag = False

if flag:
    print("Valid")
else:
    print("Invalid")