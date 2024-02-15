import sys

N, M = map(int, input().split())

board = []
monster_list = []
item_list = []
turn_count = 0

for _ in range(N):
    row = input()
    temp = []
    for i in range(0, len(row)):
        temp.append(row[i])
    board.append(temp)

move_list = input()

monster_count = 0
item_count = 0

player = {
    'row': 0,
    'col': 0,
    'level': 1,
    'hp': 20,
    'max_hp': 20,
    'att': 2,
    'add_att': 0,
    'def': 2,
    'add_def': 0,
    'exp': 0,
    'items': []
}

for i, row in enumerate(board):
    for j, info in enumerate(row):
        if info == '&' or info == 'M':
            monster_count += 1
        elif info == 'B':
            item_count += 1
        elif info == '@':
            player['row'] = i
            player['col'] = j

first_row = player['row']
first_col = player['col']


for _ in range(0, monster_count):
    monster_info = input().split()

    row = int(monster_info[0]) - 1
    col = int(monster_info[1]) - 1

    if board[row][col] == 'M':
        type = 'boss'
    else:
        type = 'normal'

    monster_list.append({
        'row': row,
        'col': col,
        'type': type,
        'name': monster_info[2],
        'att': int(monster_info[3]),
        'def': int(monster_info[4]),
        'hp': int(monster_info[5]),
        'max_hp': int(monster_info[5]),
        'exp': int(monster_info[6])
    })

for _ in range(0, item_count):
    item_info = input().split()
    item_list.append({
        'row': int(item_info[0]) - 1,
        'col': int(item_info[1]) - 1,
        'type': item_info[2],
        'effect': item_info[3]
    })


def move_player(board, player, type): 
    temp = player.copy()

    delta = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    row, col = delta[type]

    temp['row'] += row
    temp['col'] += col
    temp['row'] = max(0, min(N-1, temp['row']))
    temp['col'] = max(0, min(M-1, temp['col']))

    if board[temp['row']][temp['col']] == '#':
        return player
    
    player = temp.copy()

    return player

def find_monster(row, col):
    for monster in monster_list:
        if monster['row'] == row and monster['col'] == col:
            return monster

def find_item(row, col):
    for item in item_list:
        if item['row'] == row and item['col'] == col:
            return item

def print_player(player):
    print("LV : " + str(player['level']))
    print("HP : " + str(player['hp']) + "/" + str(player['max_hp']))
    print("ATT : " + str(player['att']) + "+" + str(player['add_att']))
    print("DEF : " + str(player['def']) + "+" + str(player['add_def']))
    print("EXP : " + str(player['exp']) + "/" + str(player['level'] * 5))

def end_game(player, type, monster=None):
    global turn_count
    
    turn_count += 1

    if type == "win" or type == "normal" :
        board[player['row']][player['col']] = "@"

    for row in board:
        temp = ""
        for item in row:
            temp += item
        print(temp)

    print("Passed Turns : " + str(turn_count))

    if type == "win":
        print_player(player)
        print("YOU WIN!")

    elif type == "lose":
        player['hp'] = 0
        print_player(player)
        print("YOU HAVE BEEN KILLED BY " + monster['name'] + "..")

    elif type == "spike":
        player['hp'] = 0
        print_player(player)
        print("YOU HAVE BEEN KILLED BY SPIKE TRAP..")
    
    elif type == "normal":
        print_player(player)
        print("Press any key to continue.")

    sys.exit(0)

def revive(player, monster=None):
    player['hp'] = player['max_hp']
    player['row'] = first_row
    player['col'] = first_col
    player['items'].remove('RE')
    if monster:
        monster['hp'] = monster['max_hp']

def check_fight_ended(player, monster):
    if player['hp'] <= 0:
        if 'RE' in player['items']:
            revive(player, monster)
            return True

        else:
            end_game(player, "lose", monster)
    
    if monster['hp'] <= 0:
        if 'HR' in player['items']:
            player['hp'] += 3
            if player['hp'] > player['max_hp']:
                player['hp'] = player['max_hp']
        
        if 'EX' in player['items']:
            player['exp'] += int(monster['exp'] * 1.2)
        else:
            player['exp'] += monster['exp']
        if player['exp'] >= (5 * player['level']):
            player['level'] += 1
            player['max_hp'] += 5
            player['att'] += 2
            player['def'] += 2
            player['hp'] = player['max_hp']
            player['exp'] = 0

        board[player['row']][player['col']] = '.'

        if monster['type'] == 'boss':
            end_game(player, "win")

        return True

def fight(player, monster):
    att_rank = 1
    hu_flag = False

    if 'CO' in player['items']:
        att_rank = 2
        if 'DX' in player['items']:
            att_rank = 3

    if 'HU' in player['items'] and monster['type'] == 'boss':
        player['hp'] = player['max_hp']
        hu_flag = True
    
    while True:
        monster['hp'] -= max(1, (att_rank * (player['att'] + player['add_att']) - monster['def']))
        att_rank = 1
        
        if check_fight_ended(player, monster):
            break
    
        if hu_flag and monster['type'] == 'boss':
            hu_flag = False
        else:
            player['hp'] -= max(1, monster['att'] - (player['def'] + player['add_def']))

        if check_fight_ended(player, monster):
            break


def fight_start(player):
    monster = find_monster(player['row'], player['col'])    
    
    fight(player, monster)


board[player['row']][player['col']] = "."

for move in move_list:
    player = move_player(board, player, move)

    if board[player['row']][player['col']] in ('&', 'M'):
        fight_start(player) 

    elif board[player['row']][player['col']] in ('^'):
        damage = 5
        if 'DX' in player['items']:
            damage = 1
        
        player['hp'] -= damage
        if player['hp'] <= 0:
            if 'RE' in player['items']:
                revive(player)
            else:
                end_game(player, 'spike')

    elif board[player['row']][player['col']] in ('B'):
        item = find_item(player['row'], player['col'])

        if item['type'] == 'W':
            player['add_att'] = int(item['effect'])
            board[player['row']][player['col']] = "."

        if item['type'] == 'A':
            player['add_def'] = int(item['effect'])
            board[player['row']][player['col']] = "."

        if item['type'] == 'O':
            if len(player['items']) < 4 and item['effect'] not in player['items']:
                player['items'].append(item['effect'])
            board[player['row']][player['col']] = "."

    turn_count += 1

turn_count -= 1
end_game(player, 'normal')