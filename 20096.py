import numpy as np

# 스도쿠 퍼즐을 2D numpy 배열로 설정
puzzle = np.array([
    [4, 0, 3, 1, 2, 9, 6, 8, 5],
    [0, 5, 9, 7, 8, 6, 3, 1, 2],
    [1, 8, 6, 4, 5, 3, 9, 7, 0],
    [3, 4, 2, 0, 0, 8, 7, 0, 6],
    [9, 1, 8, 6, 7, 0, 0, 5, 3],
    [6, 7, 5, 9, 1, 2, 4, 0, 8],
    [2, 3, 1, 8, 9, 7, 5, 6, 4],
    [8, 9, 7, 5, 6, 4, 2, 3, 1],
    [5, 6, 4, 2, 3, 1, 8, 9, 7]
])

# 빈 칸을 찾는 함수
def find_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j  # 빈 칸의 좌표를 반환
    return None

# 스도쿠 퍼즐이 유효한지 확인하는 함수
def is_valid(puzzle, num, pos):
    # 가로줄 검사
    for i in range(9):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False

    # 세로줄 검사
    for i in range(9):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False

    # 3x3 박스 검사
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == num and (i, j) != pos:
                return False

    return True

# 스도쿠 퍼즐을 푸는 함수
def solve(puzzle):
    find = find_empty(puzzle)
    if not find:
        return True  # 더 이상 빈 칸이 없으면 완료
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(puzzle, i, (row, col)):
            puzzle[row][col] = i

            if solve(puzzle):
                return True

            puzzle[row][col] = 0

    return False

# 퍼즐 풀기
solve(puzzle)
print(puzzle)