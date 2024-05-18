import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    ans = 0 #답
    check = [[False] * w for _ in range(h)] #BFS 탐색 체크 배열
    q = deque() #다음 탐색 확인 deque

    #(0,0) 부터 탐색 why? (0,0)은 내가 임의로 만든 Border
    #무조건 빈 땅임.
    q.append((0,0)) 
    check[0][0] = True

    while(q):
        next_x, next_y = q.popleft()
        for i in range(4):
            x = next_x + dx[i]
            y = next_y + dy[i]
            
            if(0 <= x < h and 0 <= y < w and board[x][y] != "*" and not check[x][y]):
                #Case 1. 탐색을 했는데, 빈 공간
                if(board[x][y] == '.'):
                    check[x][y] = True
                    q.append((x,y))

                #Case 2. 탐색을 했는데, 훔쳐야 하는 문서
                elif(board[x][y] == '$'):
                    ans += 1
                    q.append((x,y))
                    check[x][y] = True
                    board[x][y] = '.'
                else:
                    #Case 3. 탐색을 했는데, 문일 때 (알파벳 대문자)
                    if(board[x][y].isupper()):
                        #Key가 존재하면, 문을 엶
                        if(keys[ord(board[x][y].lower()) - 97]):
                            q.append((x,y))
                            board[x][y] = '.'
                            check[x][y] = True
                    #Case 4. 탐색을 했는데, 열쇠 일 때, (알파벳 소문자)
                    elif(board[x][y].islower()):
                        #key배열에 키를 추가한 다음, 싹다 초기화 후 그 좌표부터 다시 탐색
                        keys[ord(board[x][y].lower()) - 97] = True
                        board[x][y] = '.'
                        check = [[False] * w for _ in range(h)]
                        q = deque()
                        q.append((x,y))
    print(ans)

n = int(input())
for _ in range(n):

    h, w = map(int, input().split())
    board = []

    board.append(['.'] * (w+2))
    for _ in range(h):
        li = list(map(str, input().rstrip()))
        board.append(['.'] + li + ['.'])
    board.append(['.'] * (w+2))    

    key = list(map(str, input().rstrip()))
    keys = [False] * 26
    #set key
    for k in key:
        if(k == '0'):
            break
        else:
            keys[ord(k) - 97] = True
    #미리 입력 받은 key는 풀어놓음
    #여기서 1 ~ h+1 까지 탐색하는 이유는,
    #0과 h+2는 임의로 만든 구역이기 때문
    for i in range(1, h+1):
        for j in range(1, w+1):
            if(board[i][j].isupper() and keys[ord(board[i][j].lower()) - 97]):
               board[i][j] = '.'

    h += 2
    w += 2

    bfs()


