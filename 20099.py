import numpy as np

# 스도쿠 그리드를 사용자로부터 입력받는 함수
def input_sudoku():
    grid = []
    for i in range(100):
        while True:
            row = input()
            row_data = list(map(int, row.split()))
            if len(row_data) == 100:
                grid.append(row_data)
                break
            else:
                print("각 행에는 100개의 숫자를 입력해야 합니다. 다시 시도하세요.")
    return np.array(grid)

# 숫자가 해당 위치에 유효한지 확인하는 함수
def is_valid(grid, row, col, num):
    # 행에서 같은 숫자가 있는지 확인
    if num in grid[row, :]:
        return False
    
    # 열에서 같은 숫자가 있는지 확인
    if num in grid[:, col]:
        return False
    
    # 10x10 서브그리드에서 같은 숫자가 있는지 확인
    start_row, start_col = 10 * (row // 10), 10 * (col // 10)
    if num in grid[start_row:start_row + 10, start_col:start_col + 10]:
        return False
    
    return True

# 각 셀마다 가능한 숫자 후보를 업데이트하는 함수
def find_candidates(grid):
    candidates = {}
    for row in range(100):
        for col in range(100):
            if grid[row, col] == 0:
                candidates[(row, col)] = [num for num in range(1, 101) if is_valid(grid, row, col, num)]
    return candidates

# 후보가 가장 적은 셀을 선택하는 함수
def select_cell_with_fewest_candidates(candidates):
    return min(candidates, key=lambda k: len(candidates[k]))

# 백트래킹 알고리즘으로 스도쿠를 푸는 함수 (가지치기 포함)
def solve_sudoku(grid):
    # 가능한 숫자 후보를 찾음
    candidates = find_candidates(grid)
    
    # 후보가 없으면 스도쿠가 이미 해결된 상태
    if not candidates:
        return True
    
    # 후보가 가장 적은 셀을 선택
    row, col = select_cell_with_fewest_candidates(candidates)
    
    for num in candidates[(row, col)]:
        if is_valid(grid, row, col, num):
            grid[row, col] = num
            if solve_sudoku(grid):  # 재귀적으로 다음 셀로 넘어가기
                return True
            grid[row, col] = 0  # 실패 시 백트래킹
    
    return False

# 스도쿠 그리드를 입력받음
grid = input_sudoku()

# 스도쿠 풀기 시도
if solve_sudoku(grid):
    print("해결된 스도쿠:")
    print(grid)
else:
    print("해결할 수 없습니다.")
